__author__ = 'ynagai'
__date__ = '29 Jan 2013'

class PositiveInfo:
    """
    just for data structure of information of a positive data

    image_name: the image path of this information
    image_size: [x, y, c]
    people: the list of PersonInfo
    """

    image_name = None
    image_size = None
    people = []

    def __init__(self, image_name):
        """
        @param image_name the image path of this information
        """
        self.image_name = image_name
        self.people = []