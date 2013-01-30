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
        @return annotation_info information list of annotations
        """
        # return value
        annotation_info = []

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
                    person_info = PersonInfo()
                    while line:
                        if line.startswith('Center point on object %d ' % index):
                            # return value as '['X', 'Y)']'
                            center_info = line.split(': (')[1].split(', ')
                            person_info.center_x = int(center_info[0])
                            # get value as '\d+)'
                            person_info.center_y = int(center_info[1][:len(center_info[1]) - 2])
                            line = fin.readline()

                        if line.startswith('Bounding box for object %d ' % index):
                            # return value as '['Xmin, Ymin', 'Xmax, Ymax)']'
                            rect = line.split(': (')[1].split(') - (')

                            rect_min = rect[0].split(', ')
                            person_info.min_x = int(rect_min[0])
                            person_info.min_y = int(rect_min[1])

                            rect_max = rect[1].split(', ')
                            person_info.max_x = int(rect_max[0])
                            person_info.max_y = int(rect_max[1][:len(rect_max[1]) - 2])

                            positive_info.people.append(person_info)
                            break
                        line = fin.readline()
            annotation_info.append(positive_info)
        return annotation_info


    def parse(self):
        self._parse_annotation_info()