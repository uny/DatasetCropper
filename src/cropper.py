__author__ = 'ynagai'
__date__ = '29 Jan 2013'

import cv2
import sys

from annotation_parser import AnnotationParser

class App:
    """
    main run class for this project
    """

    def __init__(self):
        pass

    def run(self):
        annotation_parser = AnnotationParser()
        annotation_parser.parse()


if __name__ == '__main__':
    app = App()
    app.run()
