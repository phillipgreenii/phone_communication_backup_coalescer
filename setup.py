'''
phone_communication_backup_coalescer: Coalesces communication backup files.

Note that "python setup.py test" invokes pytest on the package. With appropriately
configured setup.cfg, this will check both xxx_test modules and docstrings.

Copyright 2015, Phillip Green II.
Licensed under MIT.
'''
from codecs import open
from os import path
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='phone_communication_backup_coalescer',

    version='0.1.0',

    description='Coalesces communication backup files.',
    long_description=long_description,

    url='https://github.com/phillipgreenii/phone_communication_backup_coalescer',

    author='Phillip Green II',
    author_email='phillip.green.ii@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Topic :: System :: Archiving :: Backup',

        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Android',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='backup sms calls android coalesce',

    packages=find_packages(exclude=['examples', 'tests']),

    include_package_data=True,

    install_requires=[],

    tests_require=['pytest'],
    cmdclass={'test': PyTest},

    extras_require = {
    }
)
