import datetime
import logging
import os
import fnmatch
import xml.etree.ElementTree as ET


class Coalescer:

    def __init__(self, controller):
        self._controller = controller

    def coalesce(self, source_dir, output_file_name):
        (files, items) = self._coalesce_files(source_dir)
        tree = self._controller.build_tree(items)
        self._write_tree(tree, output_file_name)
        return (files, len(items))

    def _coalesce_files(self, source_dir):
        processed_items = set()
        processed_files = []
        for root, dirnames, filenames in os.walk(source_dir):
            for filename in fnmatch.filter(filenames, self._controller.filename_pattern):
                absolute_path = os.path.join(root, filename)
                processed_files.append(absolute_path)
                logging.info('processing %s', absolute_path)
                try:
                    processed_items.update(self._controller.parse_file(absolute_path))
                except:
                    logging.error('Failed processing %s', absolute_path, exc_info=True)
        return (processed_files, self._controller.sort(processed_items))

    def _write_tree(self, tree, output_file_name):
        with open(output_file_name, 'w') as f:
            xml_declaration = ET.ProcessingInstruction('xml',
                                                        "version='1.0' encoding='UTF-8' standalone='yes'")
            build_info = ET.Comment('Created {}'.format(datetime.datetime.now()))
            xsl_declaration = ET.ProcessingInstruction('xml-stylesheet',
                                                        "type='text/xsl' href='{}'".format(self._controller.xsl_file_name))

            f.write(ET.tostring(xml_declaration))
            f.write(ET.tostring(build_info))
            f.write(ET.tostring(xsl_declaration))
            tree.write(f)
