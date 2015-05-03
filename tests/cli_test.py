'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2015, Phillip Green II
Licensed under MIT
'''

import unittest

import phone_communication_backup_coalescer.cli as cli


class CliTestCase(unittest.TestCase):

    def test_parse_arguments_with_empty_arguments(self):
        args = []
        with self.assertRaises(SystemExit):
            cli.parse_arguments(args)

    def test_parse_arguments_with_valid_path(self):
        args = ['tests/data']

        (process_calls, process_smses, source_dir) = cli.parse_arguments(args)
        self.assertEqual(process_calls, True)
        self.assertEqual(process_smses, True)
        self.assertEqual(source_dir, 'tests/data')

    def test_parse_arguments_with_invalid_path(self):
        args = ['potatoes']
        with self.assertRaises(SystemExit):
            cli.parse_arguments(args)

    def test_parse_arguments_with_valid_path_and_no_sms(self):
        args = ['tests/data', '--no-sms']

        (process_calls, process_smses, source_dir) = cli.parse_arguments(args)
        self.assertEqual(process_calls, True)
        self.assertEqual(process_smses, False)
        self.assertEqual(source_dir, 'tests/data')

    def test_parse_arguments_with_valid_path_and_no_calls(self):
        args = ['tests/data', '--no-calls']

        (process_calls, process_smses, source_dir) = cli.parse_arguments(args)
        self.assertEqual(process_calls, False)
        self.assertEqual(process_smses, True)
        self.assertEqual(source_dir, 'tests/data')

    def test_parse_arguments_with_valid_path_and_no_sms_and_no_calls(self):
        args = ['tests/data', '--no-calls', '--no-sms']

        (process_calls, process_smses, source_dir) = cli.parse_arguments(args)
        self.assertEqual(process_calls, False)
        self.assertEqual(process_smses, False)
        self.assertEqual(source_dir, 'tests/data')

if __name__ == '__main__':
    unittest.main()
