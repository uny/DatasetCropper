__author__ = 'ynagai'
__date__ = '29 Jan 2013'


class PersonInfo:
    """
    just for data structure of information of a person
    """
    def __init__(self, center_x=None, center_y=None,
                 min_x=None, min_y=None, max_x=None, max_y=None):
        """
        declaration for structure
        @param center_x head position x
        @param center_y head position y
        @param min_x person bounding box minimum x
        @param min_y person bounding box minimum y
        @param max_x person bounding box maximum x
        @param max_y person bounding box maximum y
        """
        self.center_x = center_x
        self.center_y = center_y
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
