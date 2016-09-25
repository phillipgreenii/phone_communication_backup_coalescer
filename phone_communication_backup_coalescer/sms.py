'''
phone_communication_backup_coalescer
Copyright 2016, Phillip Green II
Licensed under MIT.
'''

import xml.etree.ElementTree as ET
import collections
import operator
import utils

sms_fields = set(['protocol', 'address', 'date', 'type', 'subject', 'body',
                  'toa', 'sc_toa', 'service_center', 'read', 'status',
                  'locked', 'date_sent', 'readable_date', 'contact_name'])
SMS = collections.namedtuple('SMS', sms_fields)

mms_fields = set(['callback_set', 'm_id', 'reserved', 'msg_id', 'pri',
                  'app_id', 'retr_txt', 'sub_cs', 'seen', 'contact_name',
                  'sub', 'rr', 'text_only', 'ct_t', 'ct_l', 'm_size',
                  'resp_st', 'msg_box', 'retr_txt_cs', 'rpt_a', 'read',
                  'readable_date', 'ct_cls', 'deletable', 'address', 'date',
                  'hidden', 'resp_txt', 'd_rpt', 'tr_id', 'locked', 'm_type',
                  'retr_st', 'd_tm', 'st', 'm_cls', 'exp', 'v', 'date_sent',
                  'read_status', 'sim_imsi', 'spam_report', 'sim_slot',
                  'sub_id', 'safe_message', 'creator'])
MMS = collections.namedtuple('MMS', list(mms_fields) + ['parts', 'addresses'])

required_mmspart_fields = set(['name', 'seq', 'cid', 'text', 'cl', 'chset',
                               'cd', 'ctt_t', 'ctt_s', 'fn', 'ct'])
optional_mmspart_fields = set(['data'])
mmspart_fields = required_mmspart_fields | optional_mmspart_fields
MMSPart = collections.namedtuple('MMSPart', mmspart_fields)

required_mmsaddr_fields = set(['address', 'type', 'charset'])
optional_mmsaddr_fields = set([])
mmsaddr_fields = required_mmsaddr_fields | optional_mmsaddr_fields
MMSAddress = collections.namedtuple('MMSAddress', mmsaddr_fields)


def as_dict_with_out_nones(named_tuple):
    return {k: v for k, v in named_tuple._asdict().items() if v is not None}


def _build_mms(fields, parts, addresses):
    return MMS(*(fields + [tuple(parts), tuple(addresses)]))


class SmsBackupControl:

    def __init__(self):
        self.filename_pattern = 'sms*.xml'
        self.xsl_file_name = 'sms.xsl'
        self._parse_support = utils.ParseSupport()

    def sort(self, items):
        return sorted(items, key=operator.attrgetter("date"))

    def parse_file(self, file_path):
        parts = []
        addresses = []
        with open(file_path) as f:
            for (_, elem) in ET.iterparse(f):
                fields = set(elem.keys())
                if elem.tag == 'sms':
                    for warning in self._parse_support.mark_field_difference(sms_fields, fields):
                        yield {'type': 'warning', 'value': warning}
                    fields = map(elem.get, sms_fields)
                    yield {'type':'item', 'value': SMS(*fields)}
                elif elem.tag == 'part':
                    for warning in self._parse_support.mark_field_difference(required_mmspart_fields, fields, optional=optional_mmspart_fields):
                        yield {'type': 'warning', 'value': warning}
                    fields = map(elem.get, mmspart_fields)
                    parts.append(MMSPart(*fields))
                elif elem.tag == 'parts':
                    for warning in self._parse_support.mark_field_difference(set(), fields):
                        yield {'type': 'warning', 'value': warning}
                elif elem.tag == 'addr':
                    for warning in self._parse_support.mark_field_difference(required_mmsaddr_fields, fields, optional=optional_mmsaddr_fields):
                        yield {'type': 'warning', 'value': warning}
                    fields = map(elem.get, mmsaddr_fields)
                    addresses.append(MMSAddress(*fields))
                elif elem.tag == 'addrs':
                    for warning in self._parse_support.mark_field_difference(set(), fields):
                        yield {'type': 'warning', 'value': warning}
                elif elem.tag == 'mms':
                    for warning in self._parse_support.mark_field_difference(mms_fields, fields):
                        yield {'type': 'warning', 'value': warning}
                    fields = map(elem.get, mms_fields)
                    yield {'type':'item', 'value': _build_mms(fields, parts, addresses)}
                    parts = []
                    addresses = []
                elif elem.tag == 'smses':
                    pass
                else:
                    yield {'type': 'warning', 'value': 'unsupported smses tag: %s' % elem.tag}

    def sort(self, items):
        return sorted(items, key=lambda i: i.date)

    def tree_seed(self):
        root = ET.Element('smses', attrib={'count': '0'})
        tree = ET.ElementTree(root)
        return tree

    def tree_appender(self, tree, smsOrMms):
        root = tree.getroot()
        if type(smsOrMms) is SMS:
            attrs = as_dict_with_out_nones(smsOrMms)
            subelement = ET.SubElement(root, 'sms', attrib=attrs)
        elif type(smsOrMms) is MMS:
            attrs = as_dict_with_out_nones(smsOrMms)
            del attrs['parts']
            del attrs['addresses']
            mms = ET.SubElement(root, 'mms', attrib=attrs)
            parts = ET.SubElement(mms, 'parts')
            for part in smsOrMms.parts:
                attrs = as_dict_with_out_nones(part)
                ET.SubElement(parts, 'part', attrib=attrs)
            addresses = ET.SubElement(mms, 'addresses')
            for address in smsOrMms.addresses:
                attrs = as_dict_with_out_nones(address)
                ET.SubElement(addresses, 'address', attrib=attrs)
            subelement = mms
        else:
            raise Exception("unsupported sms type: %s", smsOrMms)
        root.set('count', str(int(root.get('count', '0')) + 1))
        return subelement
