__author__ = 'ynagai'
__date__ = '30 Jan 2013'

from PIL import Image

from annotation_parser import AnnotationParser

class PositiveCropper:
    """
    crop positive images
    """

    _HEAD_Y = 0.112731
    _LST_NAME = '../resources/Train/pos_person.lst'

    def __init__(self):
        pass


    def _center_head_x(self, annotation):
        """
        center head position in bounding  along x by expanding bounding box
        we call this method first
        @param annotation information of annotation
        @return annotation head-x centered annotation
        """
        for person_info in annotation.people:
            center_x = person_info.center_x
            min_x = person_info.min_x
            max_x = person_info.max_x
            # expand shorter
            if center_x - min_x < max_x - center_x:
                person_info.min_x -= max_x + min_x - 2 * center_x
            else:
                person_info.max_x += 2 * center_x - max_x - min_x
        return annotation


    def _adjust_head_y(self, annotation):
        """
        adjust head y position at (roi height) x 0.112731
        we call this method second
        @param annotation information of annotation
        @return annotation head-y adjusted annotation
        """
        for person_info in annotation.people:
            center_y = person_info.center_y
            min_y = person_info.min_y
            max_y = person_info.max_y
            # min_y + head_y is the moderate position of center_t
            head_y = (max_y - min_y) * self._HEAD_Y
            if min_y + head_y < center_y:
                # expand max_y
                person_info.max_y = int(center_y + ((center_y - min_y) * ((1 - self._HEAD_Y) / self._HEAD_Y)))
            else:
                # expand min_y
                person_info.min_y = int(center_y - (max_y - center_y) * (self._HEAD_Y / (1 - self._HEAD_Y)))
        return annotation


    def _narrow_roi_region(self, annotation, height_ratio=0.25, width_ratio=0.8):
        """
        shorten roi height when you want to restrict region for example only head
        this method is optional, if used we call it third
        @param annotation information of annotation
        @param ratio height ratio (default: 0.25)
        @return annotation roi height shortened annotation
        """
        for person_info in annotation.people:
            min_y = person_info.min_y
            max_y = person_info.max_y
            person_info.max_y = int(min_y + (max_y - min_y) * height_ratio)

            center_x = person_info.center_x
            min_x = person_info.min_x
            max_x = person_info.max_x
            person_info.min_x = int(center_x - (center_x - min_x) * width_ratio)
            person_info.max_x = int(center_x + (max_x - center_x) * width_ratio)

        return annotation


    def _adjust_region(self, person_info, ratio):
        center_x = person_info.center_x
        center_y = person_info.center_y
        min_x = person_info.min_x
        min_y = person_info.min_y
        max_x = person_info.max_x
        max_y = person_info.max_y

        person_info.min_x = int(center_x - (center_x - min_x) * ratio)
        person_info.min_y = int(center_y - (center_y - min_y) * ratio)
        person_info.max_x = int(center_x + (max_x - center_x) * ratio)
        person_info.max_y = int(center_y + (max_y - center_y) * ratio)

        return person_info


    def _check_region(self, annotation):
        """
        check roi region if it sticks out the image
        @param annotation information of annotation
        @return annotation annotation with modified roi region
        """
        for person_info in annotation.people:
            if person_info.min_x < 0:
                center_x = person_info.center_x
                min_x = person_info.min_x
                person_info = self._adjust_region(person_info, float(center_x) / (center_x - min_x))
            if person_info.min_y < 0:
                center_y = person_info.center_y
                min_y = person_info.min_y
                person_info = self._adjust_region(person_info, float(center_y) / (center_y - min_y))
            if annotation.image_size[0] < person_info.max_x:
                image_width = annotation.image_size[0]
                center_x = person_info.center_x
                max_x = person_info.max_x
                person_info = self._adjust_region(person_info, float(image_width - center_x) / (max_x - center_x))
            if annotation.image_size[1] < person_info.max_y:
                image_height = annotation.image_size[1]
                center_y = person_info.center_y
                max_y = person_info.max_y
                person_info = self._adjust_region(person_info, float(image_height - center_y) / (max_y - center_y))
        return annotation


    def _crop_image_with_annotation_and_resize(self, annotation, size=(30, 15)):
        image_name = annotation.image_name
        image = Image.open('../resources/' + image_name)
        for index in range(len(annotation.people)):
            person_info = annotation.people[index]
            person_image_name = '../resources/' + image_name.split('.')[0] + '_%d.png' % index
            person_image_name = person_image_name.replace('/pos/', '/pos_person/')

            with open(self._LST_NAME, 'a') as fout:
                fout.write(person_image_name + '\n')

            roi = (person_info.min_x, person_info.min_y, person_info.max_x, person_info.max_y)
            cropped = image.crop(roi)
            resized = cropped.resize(size, Image.BILINEAR)
            resized.save(person_image_name, 'PNG')


    def crop(self):
        """
        if you want to crop positive dataset, you use this public method
        """
        annotation_parser = AnnotationParser()
        annotation_list = annotation_parser.parse()

        # make positive person image list file
        with open(self._LST_NAME, 'w') as fout:
            fout.write('')

        for annotation in annotation_list:
            annotation = self._center_head_x(annotation)
            annotation = self._adjust_head_y(annotation)
            annotation = self._narrow_roi_region(annotation)
            annotation = self._check_region(annotation)
            self._crop_image_with_annotation_and_resize(annotation)
