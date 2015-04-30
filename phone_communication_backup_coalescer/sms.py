import xml.etree.ElementTree as ET
import collections
import logging


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


def _build_mms(fields, parts, addresses):
    return MMS(*(fields + [tuple(parts), tuple(addresses)]))


class SmsBackupControl:

    def __init__(self, parse_support):
        self.filename_pattern = 'sms*.xml'
        self._parse_support = parse_support

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

    def build_smses_tree(self, smses):
        root = ET.Element('smses', attrib={'count': str(len(smses))})
        for sms in smses:
            if type(sms) is SMS:
                attrs = dict(sms._asdict())
                ET.SubElement(root, 'sms', attrib=attrs)
            elif type(sms) is MMS:
                attrs = dict(sms._asdict())
                del attrs['parts']
                del attrs['addresses']
                if attrs['sim_imsi'] is None:
                    del attrs['sim_imsi']
                if attrs['spam_report'] is None:
                    del attrs['spam_report']
                if attrs['sim_slot'] is None:
                    del attrs['sim_slot']
                if attrs['sub_id'] is None:
                    del attrs['sub_id']
                if attrs['safe_message'] is None:
                    del attrs['safe_message']
                if attrs['creator'] is None:
                    del attrs['creator']
                mms = ET.SubElement(root, 'mms', attrib=attrs)
                parts = ET.SubElement(mms, 'parts')
                for part in sms.parts:
                    attrs = dict(part._asdict())
                    if attrs['data'] is None:
                        del attrs['data']
                    ET.SubElement(parts, 'part', attrib=attrs)
                addresses = ET.SubElement(mms, 'addresses')
                for address in sms.addresses:
                    attrs = dict(address._asdict())
                    ET.SubElement(addresses, 'address', attrib=attrs)
            else:
                raise Exception("unsupported sms type: %s", sms)
        tree = ET.ElementTree(root)
        return tree
