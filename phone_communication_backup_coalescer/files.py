'''
phone_communication_backup_coalescer
Copyright 2016, Phillip Green II
Licensed under MIT.
'''

import logging
import os
import fnmatch
from functools import partial


def _dir_to_files(file_pattern, source_dir):
    for root, dirnames, filenames in os.walk(source_dir):
        for filename in fnmatch.filter(filenames, file_pattern):
            absolute_path = os.path.join(root, filename)
            yield absolute_path


def dir_to_files_mapper(file_pattern="*"):
    d2f = partial(_dir_to_files, file_pattern)
    d2f.__doc__ = 'Maps dictories to files using the pattern of ' + file_pattern

    return d2f
