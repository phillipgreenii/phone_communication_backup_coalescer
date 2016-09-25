'''
phone_communication_backup_coalescer
Copyright 2016, Phillip Green II
Licensed under MIT.
'''

import logging
import sys

import cli

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def main():
    cli.run(sys.argv[1:])


if __name__ == "__main__":
    main()
