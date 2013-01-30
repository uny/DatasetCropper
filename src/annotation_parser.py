__author__ = 'ynagai'
__date__ = '29 Jan 2013'

from positive_info import PositiveInfo
from person_info import PersonInfo

class AnnotationParser:
    """
    parse annotation information
    """
    def __init__(self):
        pass


    def _list_path(self):
        """
        read list file and return the list
        @return annotation_list
        """
        filename = '../resources/Train/annotations.lst'
        annotation_list = []
        with open(filename, mode='r') as fin:
            line = fin.readline()
            while line:
                annotation_list.append('../resources/' + line.strip())
                line = fin.readline()
        return  annotation_list


    def _parse_annotation_info(self, filename):
        """
        parse annotation information
        @return positive_info information of parsed positive annotation
        """
        with open(name=filename, mode='r') as fin:
            line = fin.readline()
            # image filename
            while line:
                if line.startswith('Image filename'):
                    image_name = line.split('"')[1]
                    positive_info = PositiveInfo(image_name=image_name)
                    line = fin.readline()
                    break
                line = fin.readline()
            # image size
            while line:
                if line.startswith('Image size'):
                    image_size = line.split(' : ')[1].split(' x ')
                    image_size = (int(image_size[0]), int(image_size[1]), int(image_size[2]))
                    positive_info.image_size = image_size
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
                        person_info.center_y = int(center_info[1][:-2])
                        line = fin.readline()

                    if line.startswith('Bounding box for object %d ' % index):
                        # return value as '['Xmin, Ymin', 'Xmax, Ymax)']'
                        rect = line.split(': (')[1].split(') - (')

                        rect_min = rect[0].split(', ')
                        person_info.min_x = int(rect_min[0])
                        person_info.min_y = int(rect_min[1])

                        rect_max = rect[1].split(', ')
                        person_info.max_x = int(rect_max[0])
                        person_info.max_y = int(rect_max[1][:-2])

                        positive_info.people.append(person_info)
                        # next person index
                        break
                    line = fin.readline()
        return positive_info


    def parse(self):
        """
        parse given annotations
        @return annotation_list all given parsed annotation list for positive
        """
        # return value
        annotation_list = []

        for annotation_name in self._list_path():
            annotation_list.append(self._parse_annotation_info(annotation_name))

        return annotation_list
