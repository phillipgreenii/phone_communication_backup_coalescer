'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Read more here: http://pytest.org/

Copyright 2016, Phillip Green II
Licensed under MIT
'''

import unittest

from phone_communication_backup_coalescer.utils import ParseSupport, ParseWarning


class UtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.parse_support = ParseSupport()

    def test_mark_field_difference_with_missing_fields(self):
        expected_fields = set(['A', 'B', 'C', 'D'])

        warnings = self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']))
        self.assertEqual(warnings, [ParseWarning.missing_fields(['D'])])

        warnings = self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'D']))
        self.assertEqual(warnings, [ParseWarning.missing_fields(['C'])])

    def test_mark_field_difference_with_missing_fields_with_optionals(self):
        expected_fields = set(['A', 'B', 'C', 'D'])
        optional_fields = set(['E'])

        warnings = self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']), optional_fields)
        self.assertEqual(warnings, [ParseWarning.missing_fields(['D'])])

        warnings = self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'D']), optional_fields)
        self.assertEqual(warnings, [ParseWarning.missing_fields(['C'])])

    def test_mark_field_difference_with_extra_fields(self):
        expected_fields = set(['A', 'B'])

        warnings = self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']))
        self.assertEqual(warnings, [ParseWarning.extra_fields(['C'])])

        warnings = self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'D']))
        self.assertEqual(warnings, [ParseWarning.extra_fields(['D'])])

    def test_mark_field_difference_with_extra_fields_with_optionals(self):
        expected_fields = set(['A', 'B'])
        optional_fields = set(['C'])

        warnings = self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']), optional_fields)
        self.assertEqual(warnings, [])

        warnings = self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'D']), optional_fields)
        self.assertEqual(warnings, [ParseWarning.extra_fields(['D'])])


if __name__ == '__main__':
    unittest.main()
