'''
phone_communication_backup_coalescer
Copyright 2016, Phillip Green II
Licensed under MIT.
'''

import xml.etree.ElementTree as ET
import collections
import operator
import utils

call_fields = set(['number', 'duration', 'date', 'type', 'readable_date',
                   'contact_name'])

Call = collections.namedtuple('Call', call_fields)


class CallsBackupControl:

    def __init__(self):
        self.filename_pattern = 'calls*.xml'
        self.xsl_file_name = 'calls.xsl'
        self._parse_support = utils.ParseSupport()

    def parse_file(self, file_path):
        with open(file_path) as f:
            for (_, elem) in ET.iterparse(f):
                fields = set(elem.keys())
                if elem.tag == 'call':
                    for warning in self._parse_support.mark_field_difference(call_fields, fields):
                        yield {'type': 'warning', 'value': warning}
                    fields = map(elem.get, call_fields)
                    yield {'type':'item', 'value': Call(*fields)}
                elif elem.tag == 'calls':
                    pass
                else:
                    yield {'type': 'warning', 'value': 'unsupported calls tag: %s' % elem.tag}

    def sort(self, items):
        return sorted(items, key=lambda i: i.date)

    def tree_seed(self):
        root = ET.Element('calls', attrib={'count': '0'})
        tree = ET.ElementTree(root)
        return tree

    def tree_appender(self, tree, call):
        root = tree.getroot()
        subelement = ET.SubElement(root, 'call', attrib=call._asdict())
        root.set('count', str(int(root.get('count', '0')) + 1))
        return subelement
