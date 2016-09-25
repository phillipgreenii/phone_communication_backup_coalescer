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

from phone_communication_backup_coalescer.coalesce import Coalescer
from phone_communication_backup_coalescer.sms import SmsBackupControl


class SmsCoalescerTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp('coalescer-sms-test')
        self.source_dir = os.path.join('tests', 'data')

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def assert_file_exists(self, path):
        if not os.path.isfile(path):
            raise AssertionError(path + " is not a file")

    def test_coalesce_calls_works(self):
        output_file = os.path.join(self.temp_dir, "full-sms-test.xml")

        coalescer = Coalescer(SmsBackupControl())

        (files, item_count) = coalescer.coalesce(self.source_dir, output_file)

        self.assert_file_exists(output_file)
        self.assertEqual(files, ['tests/data/sms-test.xml'])
        self.assertEqual(item_count, 15)


if __name__ == '__main__':
    unittest.main()
