import xml.etree.ElementTree as ET
import collections
import logging
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
        smses = []
        parts = []
        addresses = []
        with open(file_path) as f:
            for (_, elem) in ET.iterparse(f):
                fields = set(elem.keys())
                if elem.tag == 'sms':
                    self._parse_support.mark_field_difference(sms_fields, fields)
                    fields = map(elem.get, sms_fields)
                    smses.append(SMS(*fields))
                elif elem.tag == 'part':
                    self._parse_support.mark_field_difference(required_mmspart_fields, fields, optional=optional_mmspart_fields)
                    fields = map(elem.get, mmspart_fields)
                    parts.append(MMSPart(*fields))
                elif elem.tag == 'parts':
                    self._parse_support.mark_field_difference(set(), fields)
                    pass
                elif elem.tag == 'addr':
                    self._parse_support.mark_field_difference(required_mmsaddr_fields, fields, optional=optional_mmsaddr_fields)
                    fields = map(elem.get, mmsaddr_fields)
                    addresses.append(MMSAddress(*fields))
                elif elem.tag == 'addrs':
                    self._parse_support.mark_field_difference(set(), fields)
                    pass
                elif elem.tag == 'mms':
                    self._parse_support.mark_field_difference(mms_fields, fields)
                    fields = map(elem.get, mms_fields)
                    smses.append(_build_mms(fields, parts, addresses))
                    parts = []
                    addresses = []
                elif elem.tag == 'smses':
                    pass
                else:
                    logging.warn('unsupported tag: %s', elem.tag)
        return smses

    def build_tree(self, smses):
        root = ET.Element('smses', attrib={'count': str(len(smses))})
        for sms in smses:
            if type(sms) is SMS:
                attrs = as_dict_with_out_nones(sms)
                ET.SubElement(root, 'sms', attrib=attrs)
            elif type(sms) is MMS:
                attrs = as_dict_with_out_nones(sms)
                del attrs['parts']
                del attrs['addresses']
                mms = ET.SubElement(root, 'mms', attrib=attrs)
                parts = ET.SubElement(mms, 'parts')
                for part in sms.parts:
                    attrs = as_dict_with_out_nones(part)
                    ET.SubElement(parts, 'part', attrib=attrs)
                addresses = ET.SubElement(mms, 'addresses')
                for address in sms.addresses:
                    attrs = as_dict_with_out_nones(address)
                    ET.SubElement(addresses, 'address', attrib=attrs)
            else:
                raise Exception("unsupported sms type: %s", sms)
        tree = ET.ElementTree(root)
        return tree

    def warnings(self):
        return self._parse_support.items()
