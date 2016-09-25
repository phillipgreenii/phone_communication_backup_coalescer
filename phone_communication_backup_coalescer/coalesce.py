'''
phone_communication_backup_coalescer
Copyright 2016, Phillip Green II
Licensed under MIT.
'''

import datetime
import logging
import rx
from rx.core import AnonymousObservable
import xml.etree.ElementTree as ET
from phone_communication_backup_coalescer.files import dir_to_files_mapper
from phone_communication_backup_coalescer import __version__, __name__

def as_list(item):
    if not hasattr(item, '__iter__'):
        item = [item]
    return item


class Coalescer:

    def __init__(self, controller):
        self._controller = controller

    def coalesce(self, source_dirs, output_file_name):
        def write_tree(tree):
            with open(output_file_name, 'w') as f:
                xml_declaration = ET.ProcessingInstruction('xml',
                                                            "version='1.0' encoding='UTF-8' standalone='yes'")
                build_info = ET.Comment('Created by {} v{} on {}'.format(__name__, __version__, datetime.datetime.now()))
                xsl_declaration = ET.ProcessingInstruction('xml-stylesheet',
                                                            "type='text/xsl' href='{}'".format(self._controller.xsl_file_name))
                f.write(ET.tostring(xml_declaration))
                f.write(ET.tostring(build_info))
                f.write(ET.tostring(xsl_declaration))
                tree.write(f)

        def append_item_to_tree(root, item):
            self._controller.tree_appender(root, item)
            return root
        meta = [[], 0]

        def rememberFile(f):
            meta[0].append(f)

        def safely_parse(f):
            def subscribe(observer):
                try:
                    items = list(self._controller.parse_file(f))
                except Exception as ex:
                    error = {'type': 'error', 'value': ex, 'file': f}
                    observer.on_next(error)
                    observer.on_completed()
                    return

                for item in items:
                    observer.on_next(item)
                observer.on_completed()

            return AnonymousObservable(subscribe)

        def increment_counter(_):
            meta[1] += 1

        def print_errors(e):
            if e['type'] == 'error':
                logging.error('Error: %s', e['value'])


        # TODO print warnings
        source = rx.Observable.from_iterable(as_list(source_dirs))\
            .flat_map(dir_to_files_mapper(self._controller.filename_pattern))\
            .distinct()\
            .do_action(rememberFile)\
            .do_action(lambda f: logging.info('processing %s', f))\
            .flat_map(safely_parse)\
            .do_action(print_errors)\
            .where(lambda e: e['type'] == 'item')\
            .map(lambda e: e['value'])\
            .distinct()\
            .do_action(increment_counter)\
            .to_list()\
            .flat_map(lambda l: self._controller.sort(l))\
            .reduce(append_item_to_tree, self._controller.tree_seed())\
            .do_action(lambda _: logging.info('writing %s', output_file_name))\
            .subscribe(write_tree)

        return tuple(meta)
