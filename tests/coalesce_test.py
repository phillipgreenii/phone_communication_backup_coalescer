'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Read more here: http://pytest.org/

Copyright 2016, Phillip Green II
Licensed under MIT
'''

import unittest
import xml.etree.ElementTree as ET
import os.path
import tempfile
import shutil
import datetime

from phone_communication_backup_coalescer.coalesce import Coalescer


class CoalescerTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp('coalescer-test')
        self.source_dir = os.path.join('tests', 'data')
        self.test_tree = ET.ElementTree(ET.Element('items', attrib={'count': str(0)}))

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def assert_file_exists(self, path):
        if not os.path.isfile(path):
            raise AssertionError(path + " is not a file")

    def assert_starts_with(self, actual_string, expected_start):
        if not actual_string.startswith(expected_start):
            raise AssertionError(actual_string + " does not start with '" + expected_start + "'")

    def assert_ends_with(self, actual_string, expected_end):
        if not actual_string.endswith(expected_end):
            raise AssertionError(actual_string + " does not end with '" + expected_end + "'")

    def test_coalesce_tree_with_appropriate_headers(self):
        output_file = os.path.join(self.temp_dir, "tree-test.xml")
        expected_start = '<?xml version=\'1.0\' encoding=\'UTF-8\' standalone=\'yes\'?><!--Created '
        # NOTE: The middle is the timestamp which can't be known
        expected_end = '--><?xml-stylesheet type=\'text/xsl\' href=\'fake.xsl\'?><items count="0" />'

        coalescer = Coalescer(SimpleController())

        coalescer.coalesce([], output_file)

        self.assert_file_exists(output_file)
        tree_as_file = readFile(output_file)
        self.assert_starts_with(tree_as_file, expected_start)
        self.assert_ends_with(tree_as_file, expected_end)

    def test_coalesce_works(self):
        output_file = os.path.join(self.temp_dir, "full-test.xml")

        coalescer = Coalescer(SimpleController())

        (files, item_count) = coalescer.coalesce(self.source_dir, output_file)

        self.assert_file_exists(output_file)
        self.assertEqual(files, ['tests/data/calls-test.xml', 'tests/data/sms-test.xml'])
        self.assertEqual(item_count, 2)

    def test__coalesce_files_continues_on_failed_parsing(self):
        output_file = os.path.join(self.temp_dir, "full-test.xml")

        coalescer = Coalescer(FailingController())

        (files, item_count) = coalescer.coalesce(self.source_dir, output_file)

        self.assert_file_exists(output_file)
        self.assertEqual(files, ['tests/data/calls-test.xml', 'tests/data/sms-test.xml'])
        self.assertEqual(item_count, 0)


def readFile(path):
    with open(path) as f:
        return f.read()


class SimpleController:
    def __init__(self):
        self.filename_pattern = "*.xml"
        self.xsl_file_name = 'fake.xsl'

    def parse_file(self, file_path):
        item = {'file': file_path, 'data': 'data'}
        yield {'type': 'item', 'value': item}

    def sort(self, items):
        return sorted(items, key=lambda i: i['file'])

    def tree_seed(self):
        root = ET.Element('items', attrib={'count': '0'})
        tree = ET.ElementTree(root)
        return tree

    def tree_appender(self, tree, item):
        root = tree.getroot()
        subelement = ET.SubElement(root, 'item', attrib=item)
        root.set('count', str(int(root.get('count', '0')) + 1))
        return subelement


class FailingController(SimpleController):
    def __init__(self):
        self.filename_pattern = "*.xml"
        self.xsl_file_name = 'error.xsl'

    def parse_file(self, file_path):
        raise Exception("Failure Parsing")


if __name__ == '__main__':
    unittest.main()
