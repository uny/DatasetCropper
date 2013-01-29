__author__ = 'ynagai'
__date__ = '29 Jan 2013'

import sys
import re

from positive_info import PositiveInfo
import person_info

class AnnotationParser:
    """
    parse annotation information
    """
    def __init__(self):
        pass


    def _list_path(self, target=None):
        """
        read list file and return the list
        @param target option: annotations.lst, neg.lst, pos.lst
        @return annotation_list
        """
        if target == None:
            sys.stderr.write('target is not selected in _line_path method\n')
            return []
        filename = '../resources/Train/' + target
        annotation_list = []
        with open(name=filename, mode='r') as fin:
            line = fin.readline()
            while line:
                annotation_list.append('../resources/' + line.strip())
                line = fin.readline()
        return  annotation_list


    def _parse_annotation_info(self):
        """
        parse annotation information
        @return
        """
        annotation_list = self._list_path(target='annotations.lst')
        for annotation_name in annotation_list:
            with open(name=annotation_name, mode='r') as fin:
                content = fin.read()
            image_name = re.search(pattern='Image filename : "[\w\./]+"', string=content).group(0)
            positive_info = PositiveInfo(image_name=image_name)




    def parse(self):
        self._parse_annotation_info()