'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2015, Phillip Green II
Licensed under MIT
'''

import StringIO


class BuildTreeAssertions:

    def assert_tree_as_string(self, tree, string):
        string_stream = StringIO.StringIO()
        tree.write(string_stream)

        tree_as_string = string_stream.getvalue()
        string_stream.close()
        # HACK (this only works if testing class subclasses unittest.TestCase)
        self.assertEqual(tree_as_string, string)
