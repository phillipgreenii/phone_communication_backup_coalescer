import xml.etree.ElementTree as ET
import collections
import logging


call_fields = set(['number', 'duration', 'date', 'type', 'readable_date',
                   'contact_name'])

Call = collections.namedtuple('Call', call_fields)


class CallsBackupControl:

    def __init__(self, parse_support):
        self.filename_pattern = 'calls*.xml'
        self._parse_support = parse_support

    def parse_file(self, file_path):
        calls = []
        with open(file_path) as f:
            for (_, elem) in ET.iterparse(f):
                fields = set(elem.keys())
                if elem.tag == 'call':
                    self._parse_support.mark_field_difference(call_fields, fields)
                    fields = map(elem.get, call_fields)
                    calls.append(Call(*fields))
                elif elem.tag == 'calls':
                    pass
                else:
                    logging.warn('unsupported tag: %s', elem.tag)
        return calls

    def build_calls_tree(self, calls):
        root = ET.Element('calls', attrib={'count': str(len(calls))})
        for call in calls:
            ET.SubElement(root, 'call', attrib=call._asdict())
        tree = ET.ElementTree(root)
        return tree
