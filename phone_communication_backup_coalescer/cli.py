import logging
import argparse
import collections
import sys
import os

import sms
import calls
import coalesce


def is_dir(dirname):
    """Checks if a path is an actual directory"""
    if not os.path.isdir(dirname):
        msg = "{0} is not a directory".format(dirname)
        raise argparse.ArgumentTypeError(msg)
    else:
        return dirname


def parse_arguments(arguments):
    parser = argparse.ArgumentParser(prog='phone_communication_backup_coalescer',
                                     description='Coalesce backup files.')
    parser.add_argument('rootDirectoryToSearch', type=is_dir,
                        help='path to search for backup files')
    parser.add_argument('--no-sms', dest='coalesce_sms', action='store_false',
                        help='disables coalescing of SMS')
    parser.add_argument('--no-calls', dest='coalesce_calls', action='store_false',
                        help='disables coalescing of calls')
    parser.set_defaults(coalesce_sms=True, coalesce_calls=True)

    args = parser.parse_args(arguments)
    return (args.coalesce_calls, args.coalesce_sms, args.rootDirectoryToSearch)


CoalescerInfo = collections.namedtuple('CoalescerInfo', ['controller', 'output_file_name'])


def cli(process_calls, process_smses, source_dir):
    infos = {}

    if process_calls:
        infos['calls'] = CoalescerInfo(calls.CallsBackupControl(), 'coalesced-calls.xml')

    if process_smses:
        infos['smses'] = CoalescerInfo(sms.SmsBackupControl(), 'coalesced-smses.xml')

    for key, info in infos.items():
        logging.info('Coalescing %s', key)
        coalescer = coalesce.Coalescer(info.controller)
        coalescer.coalesce(source_dir, info.output_file_name)
        for warning, count in info.controller.warnings():
            logging.warn("%s: %i", warning, count)


def run(args):
    cli(*parse_arguments(args))
