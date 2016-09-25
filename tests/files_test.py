'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Read more here: http://pytest.org/

Copyright 2016, Phillip Green II
Licensed under MIT
'''

import unittest
import os.path

from phone_communication_backup_coalescer.files import dir_to_files_mapper


class FilesTestCase(unittest.TestCase):
    def setUp(self):
        self.source_dir = os.path.join('tests', 'data')

    def test_dir_to_files_mapper_should_return_all_files(self):

        files = list(dir_to_files_mapper("*.xml")(self.source_dir))

        self.assertEqual(files, ['tests/data/calls-test.xml', 'tests/data/sms-test.xml'])

if __name__ == '__main__':
    unittest.main()
