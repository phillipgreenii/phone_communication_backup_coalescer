'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Read more here: http://pytest.org/

Copyright 2016, Phillip Green II
Licensed under MIT
'''

import unittest
import os.path
import tempfile
import shutil
import datetime

from phone_communication_backup_coalescer.calls import CallsBackupControl, Call


class CallsTestCase(unittest.TestCase):
    def setUp(self):
        self.backup_control = CallsBackupControl()

    def test_contract(self):
        self.assertIsNotNone(self.backup_control.filename_pattern)
        self.assertIsNotNone(self.backup_control.xsl_file_name)
        self.assertIsNotNone(self.backup_control.parse_file)
        self.assertIsNotNone(self.backup_control.tree_seed)
        self.assertIsNotNone(self.backup_control.tree_appender)

    def test_tree_seed_should_initialize_element_tree_with_root_of_calls(self):
        element_tree = self.backup_control.tree_seed()

        self.assertEqual(element_tree.getroot().tag, 'calls')

    def test_tree_seed_should_initialize_element_tree_with_count_of_0(self):
        element_tree = self.backup_control.tree_seed()

        self.assertEqual(element_tree.getroot().get('count'), '0')

    def test_parse_file(self):
        full_file_name = os.path.join('tests', 'data', 'calls-test.xml')
        # warnings are tested in a different test
        calls = filter(lambda x: x['type'] == 'item', self.backup_control.parse_file(full_file_name))

        self.assertEqual(len(calls), 22)
        call0 = Call(
                                        readable_date='Sep 16, 2014 11:31:45 AM',
                                        number='5555550000',
                                        date='1410881505425',
                                        duration='0',
                                        contact_name='(Unknown)',
                                        type='3')
        self.assertEqual(calls[0], {'type': 'item', 'value': call0})
        call1 = Call(
                                        readable_date='Sep 16, 2014 1:03:03 PM',
                                        number='5555550001',
                                        date='1410886983207',
                                        duration='38',
                                        contact_name='John Stuart',
                                        type='1')
        self.assertEqual(calls[1], {'type': 'item', 'value': call1})
        call2 = Call(
                                        readable_date='Sep 18, 2014 11:24:10 AM',
                                        number='5555550001',
                                        date='1411053850787',
                                        duration='43',
                                        contact_name='John Stuart',
                                        type='1')
        self.assertEqual(calls[2], {'type': 'item', 'value': call2})
        call3 = Call(
                                        readable_date='Sep 19, 2014 4:45:16 PM',
                                        number='5555550003',
                                        date='1411159516747',
                                        duration='0',
                                        contact_name='Jack Daniels',
                                        type='3')
        self.assertEqual(calls[3], {'type': 'item', 'value': call3})
        call4 = Call(
                                        readable_date='Sep 20, 2014 9:33:25 AM',
                                        number='5555550004',
                                        date='1411220005294',
                                        duration='39',
                                        contact_name='Oscar Wilde',
                                        type='1')
        self.assertEqual(calls[4], {'type': 'item', 'value': call4})
        call5 = Call(
                                        readable_date='Sep 21, 2014 9:28:35 AM',
                                        number='5555550004',
                                        date='1411306115904',
                                        duration='20',
                                        contact_name='Oscar Wilde',
                                        type='1')
        self.assertEqual(calls[5], {'type': 'item', 'value': call5})
        call6 = Call(
                                        readable_date='Sep 21, 2014 4:32:48 PM',
                                        number='5555550004',
                                        date='1411331568231',
                                        duration='130',
                                        contact_name='Oscar Wilde',
                                        type='2')
        self.assertEqual(calls[6], {'type': 'item', 'value': call6})
        call7 = Call(
                                        readable_date='Oct 21, 2014 9:47:07 AM',
                                        number='15555550014',
                                        date='1413899227828',
                                        duration='576',
                                        contact_name='(Unknown)',
                                        type='2')
        self.assertEqual(calls[7], {'type': 'item', 'value': call7})
        call8 = Call(
                                        readable_date='Oct 21, 2014 5:57:04 PM',
                                        number='5555550008',
                                        date='1413928624905',
                                        duration='0',
                                        contact_name='Cindy Lauper',
                                        type='3')
        self.assertEqual(calls[8], {'type': 'item', 'value': call8})
        call9 = Call(
                                        readable_date='Oct 21, 2014 6:39:12 PM',
                                        number='5555550008',
                                        date='1413931152037',
                                        duration='142',
                                        contact_name='Cindy Lauper',
                                        type='2')
        self.assertEqual(calls[9], {'type': 'item', 'value': call9})
        call10 = Call(
                                        readable_date='Nov 3, 2014 5:34:13 PM',
                                        number='+15555550013',
                                        date='1415054053956',
                                        duration='33',
                                        contact_name='Cindy Lauper',
                                        type='2')
        self.assertEqual(calls[10], {'type': 'item', 'value': call10})
        call11 = Call(
                                        readable_date='Nov 3, 2014 6:33:03 PM',
                                        number='+15555550015',
                                        date='1415057583749',
                                        duration='20',
                                        contact_name='(Unknown)',
                                        type='2')
        self.assertEqual(calls[11], {'type': 'item', 'value': call11})
        call12 = Call(
                                        readable_date='Nov 3, 2014 6:33:39 PM',
                                        number='+15555550015',
                                        date='1415057619663',
                                        duration='22',
                                        contact_name='(Unknown)',
                                        type='2')
        self.assertEqual(calls[12], {'type': 'item', 'value': call12})
        call13 = Call(
                                        readable_date='Dec 1, 2014 7:37:08 PM',
                                        number='5555550016',
                                        date='1417480628929',
                                        duration='0',
                                        contact_name='(Unknown)',
                                        type='3')
        self.assertEqual(calls[13], {'type': 'item', 'value': call13})
        call14 = Call(
                                        readable_date='Dec 3, 2014 11:37:41 AM',
                                        number='5555550017',
                                        date='1417624661510',
                                        duration='123',
                                        contact_name='(Unknown)',
                                        type='2')
        self.assertEqual(calls[14], {'type': 'item', 'value': call14})
        call15 = Call(
                                        readable_date='Dec 3, 2014 2:23:57 PM',
                                        number='5555550018',
                                        date='1417634637883',
                                        duration='505',
                                        contact_name='(Unknown)',
                                        type='2')
        self.assertEqual(calls[15], {'type': 'item', 'value': call15})
        call16 = Call(
                                        readable_date='Dec 3, 2014 6:21:06 PM',
                                        number='+15555550013',
                                        date='1417648866955',
                                        duration='43',
                                        contact_name='Cindy Lauper',
                                        type='2')
        self.assertEqual(calls[16], {'type': 'item', 'value': call16})
        call17 = Call(
                                        readable_date='Dec 3, 2014 10:32:27 PM',
                                        number='5555550019',
                                        date='1417663947773',
                                        duration='86',
                                        contact_name='(Unknown)',
                                        type='2')
        self.assertEqual(calls[17], {'type': 'item', 'value': call17})
        call18 = Call(
                                        readable_date='Apr 16, 2015 10:50:19 AM',
                                        number='5555550027',
                                        date='1429195819560',
                                        duration='0',
                                        contact_name='(Unknown)',
                                        type='3')
        self.assertEqual(calls[18], {'type': 'item', 'value': call18})
        call19 = Call(
                                        readable_date='Apr 16, 2015 6:29:06 PM',
                                        number='5555550028',
                                        date='1429223346465',
                                        duration='0',
                                        contact_name='(Unknown)',
                                        type='3')
        self.assertEqual(calls[19], {'type': 'item', 'value': call19})
        call20 = Call(
                                        readable_date='Apr 17, 2015 5:06:13 PM',
                                        number='5555550029',
                                        date='1429304773088',
                                        duration='36',
                                        contact_name='(Unknown)',
                                        type='2')
        self.assertEqual(calls[20], {'type': 'item', 'value': call20})
        call21 = Call(
                                        readable_date='Apr 17, 2015 9:15:42 PM',
                                        number='5555550001',
                                        date='1429319742235',
                                        duration='1001',
                                        contact_name='John Stuart',
                                        type='1')
        self.assertEqual(calls[21], {'type': 'item', 'value': call21})

    def test_parse_file_warnings(self):
        expected_warnings = []

        full_file_name = os.path.join('tests', 'data', 'calls-test.xml')
        # items are tested in a different test
        warnings = filter(lambda x: x['type'] == 'warning', self.backup_control.parse_file(full_file_name))

        self.assertEquals(warnings, expected_warnings)

    def test_tree_appender_should_add_call_element_to_root(self):
        element_tree = self.backup_control.tree_seed()
        call = Call(
                    readable_date='Apr 17, 2015 5:06:13 PM',
                    number='5555550029',
                    date='1429304773088',
                    duration='36',
                    contact_name='(Unknown)',
                    type='2')

        subelement = self.backup_control.tree_appender(element_tree, call)
        self.assertEquals(element_tree.find('call'), subelement)

    def test_tree_appender_should_create_element_with_correct_attributes(self):
        element_tree = self.backup_control.tree_seed()
        call = Call(
                    readable_date='Apr 17, 2015 5:06:13 PM',
                    number='5555550029',
                    date='1429304773088',
                    duration='36',
                    contact_name='(Unknown)',
                    type='2')

        subelement = self.backup_control.tree_appender(element_tree, call)
        self.assertEquals(subelement.get('readable_date'), 'Apr 17, 2015 5:06:13 PM')
        self.assertEquals(subelement.get('number'), '5555550029')
        self.assertEquals(subelement.get('date'), '1429304773088')
        self.assertEquals(subelement.get('duration'), '36')
        self.assertEquals(subelement.get('contact_name'), '(Unknown)')
        self.assertEquals(subelement.get('type'), '2')

    def test_tree_appender_should_increment_count_on_root(self):
        element_tree = self.backup_control.tree_seed()
        call = Call(
                    readable_date='Apr 17, 2015 5:06:13 PM',
                    number='5555550029',
                    date='1429304773088',
                    duration='36',
                    contact_name='(Unknown)',
                    type='2')

        subelement = self.backup_control.tree_appender(element_tree, call)

        self.assertEquals(element_tree.getroot().get('count'), '1')

if __name__ == '__main__':
    unittest.main()
