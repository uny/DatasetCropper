__author__ = 'ynagai'
__date__ = '29 Jan 2013'

class PositiveInfo:
    """
    just for data structure of information of a positive data
    """
    def __init__(self, image_name):
        """
        declaration for structure
        self.people is a list of PersonInfo
        @param image_name the image path of this information
        """
        self.image_name = image_name
        self.people = []