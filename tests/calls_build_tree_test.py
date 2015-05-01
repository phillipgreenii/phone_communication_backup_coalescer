'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2015, Phillip Green II
Licensed under MIT
'''

import unittest

from phone_communication_backup_coalescer.calls import CallsBackupControl, Call
from phone_communication_backup_coalescer.utils import ParseSupport

import StringIO


class BuildTreeAssertions:

    def assert_tree_as_string(self, tree, string):
        string_stream = StringIO.StringIO()
        tree.write(string_stream)

        tree_as_string = string_stream.getvalue()
        string_stream.close()
        self.assertEqual(tree_as_string, string)#HACK


class CallsBuildTreeTestCase(unittest.TestCase, BuildTreeAssertions):

    def setUp(self):
        self.backup_control = CallsBackupControl(ParseSupport())

    def test_build_tree_with_no_calls(self):
        calls = []
        expected_string = '<calls count="0" />'

        tree = self.backup_control.build_tree(calls)

        self.assert_tree_as_string(tree, expected_string)

    def test_build_tree(self):
        calls = [
            Call(
                readable_date='Sep 16, 2014 11:31:45 AM',
                number='5555550000',
                date='1410881505425',
                duration='0',
                contact_name='(Unknown)',
                type='3'),
            Call(
                readable_date='Sep 16, 2014 1:03:03 PM',
                number='5555550001',
                date='1410886983207',
                duration='38',
                contact_name='John Stuart',
                type='1'),
            Call(
                readable_date='Oct 21, 2014 9:47:07 AM',
                number='15555550014',
                date='1413899227828',
                duration='576',
                contact_name='(Unknown)',
                type='2')
        ]
        expected_string = \
            '<calls count="3">' + \
            '<call contact_name="(Unknown)" date="1410881505425" duration="0" number="5555550000" readable_date="Sep 16, 2014 11:31:45 AM" type="3" />' + \
            '<call contact_name="John Stuart" date="1410886983207" duration="38" number="5555550001" readable_date="Sep 16, 2014 1:03:03 PM" type="1" />' + \
            '<call contact_name="(Unknown)" date="1413899227828" duration="576" number="15555550014" readable_date="Oct 21, 2014 9:47:07 AM" type="2" />' + \
            '</calls>'

        tree = self.backup_control.build_tree(calls)

        self.assert_tree_as_string(tree, expected_string)

if __name__ == '__main__':
    unittest.main()
