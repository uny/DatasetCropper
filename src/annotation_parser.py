__author__ = 'ynagai'
__date__ = '29 Jan 2013'

import sys
import re

from positive_info import PositiveInfo
from person_info import PersonInfo

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
                line = fin.readline()
                # image filename
                while line:
                    if line.startswith('Image filename'):
                        image_name = line.split('"')[1]
                        positive_info = PositiveInfo(image_name=image_name)
                        line = fin.readline()
                        break
                    line = fin.readline()
                # the number of objects
                while line:
                    if line.startswith('Objects with ground truth'):
                        num_objects = int(line.split(' ')[5])
                        line = fin.readline()
                        break
                    line = fin.readline()
                # people
                for index in range(1, num_objects + 1):
                    while line:
                        if line.startswith('Center point on object %d' % index):
                            # TODO: parse here
                            pass
#            image_name = re.search(pattern=r'Image filename : "([\w\./]+)"', string=content).group(1)
#            positive_info = PositiveInfo(image_name=image_name)
#            num_objects = int(re.search(pattern=r'Objects with ground truth : (\d+)', string=content).group(1))
#            for index in range(1, num_objects + 1):
#                pattern = r'Center point on object %d "PASperson" \(X, Y\) : \((\d+), (\d+)\)' % index
#                match = re.search(pattern=pattern, string=content)



    def parse(self):
        self._parse_annotation_info()