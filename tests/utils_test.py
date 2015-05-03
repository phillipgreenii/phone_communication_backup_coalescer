'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2015, Phillip Green II
Licensed under MIT
'''

import unittest

from phone_communication_backup_coalescer.utils import ParseSupport, ParseWarning


class UtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.parse_support = ParseSupport()

    def test_mark_field_difference_with_missing_fields(self):
        expected_fields = set(['A', 'B', 'C', 'D'])

        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']))
        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'D']))
        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']))

        self.assertDictEqual(self.parse_support.as_dict(), {
            ParseWarning.missing_fields(['D']): 2,
            ParseWarning.missing_fields(['C']): 1})

    def test_mark_field_difference_with_missing_fields_with_optionals(self):
        expected_fields = set(['A', 'B', 'C', 'D'])
        optional_fields = set(['E'])

        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']), optional_fields)
        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'D']), optional_fields)
        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']), optional_fields)

        self.assertDictEqual(self.parse_support.as_dict(), {
            ParseWarning.missing_fields(['D']): 2,
            ParseWarning.missing_fields(['C']): 1})

    def test_mark_field_difference_with_extra_fields(self):
        expected_fields = set(['A', 'B'])

        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']))
        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'D']))
        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']))

        self.assertDictEqual(self.parse_support.as_dict(), {
            ParseWarning.extra_fields(['D']): 1,
            ParseWarning.extra_fields(['C']): 2})

    def test_mark_field_difference_with_extra_fields_with_optionals(self):
        expected_fields = set(['A', 'B'])
        optional_fields = set(['C'])

        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']), optional_fields)
        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'D']), optional_fields)
        self.parse_support.mark_field_difference(expected_fields, set(['A', 'B', 'C']), optional_fields)

        self.assertDictEqual(self.parse_support.as_dict(), {
            ParseWarning.extra_fields(['D']): 1})


if __name__ == '__main__':
    unittest.main()
