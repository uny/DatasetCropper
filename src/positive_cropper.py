__author__ = 'ynagai'
__date__ = '30 Jan 2013'

from annotation_parser import AnnotationParser

class PositiveCropper:
    """
    crop positive images
    """

    def __init__(self):
        pass


    def _center_head_x(self):
        """
        center head position in bounding  along x
        we call this method first
        """

        pass


    def crop(self):
        annotation_parser = AnnotationParser()
        annotation_list = annotation_parser.parse()
        print len(annotation_list)
