__author__ = 'ynagai'
__date__ = '29 Jan 2013'

import cv2
import sys

from positive_cropper import PositiveCropper

class App:
    """
    main run class for this project
    """

    def __init__(self):
        pass

    def run(self):
        positive_cropper = PositiveCropper()
        positive_cropper.crop()


if __name__ == '__main__':
    app = App()
    app.run()
