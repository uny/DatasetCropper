__author__ = 'ynagai'
__date__ = '30 Jan 2013'

import random

from PIL import Image

class NegativeCropper:
    """
    crop positive images
    """

    _LST_NAME = '../resources/Train/neg_cropped.lst'

    def __init__(self):
        pass


    def _list_negative(self):
        """
        read list file and return the list
        @return negative_list
        """
        # return value
        negative_list = []
        filename = '../resources/Train/neg.lst'
        with open(filename, 'r') as fin:
            line = fin.readline()
            while line:
                negative_list.append('../resources/' + line.strip())
                line = fin.readline()
        return negative_list


    def _random_crop_rect(self, image_size, crop_size=(90, 45)):
        """
        @return crop_rect the rect for cropping
        """
        min_x = random.randint(0, image_size[0] - crop_size[0])
        min_y = random.randint(0, image_size[1] - crop_size[1])

        crop_rect = (min_x, min_y, min_x + crop_size[0], min_y + crop_size[1])

        return crop_rect


    def _crop_and_resize_image(self, image, size=(30, 15)):
        """
        crop and resize image
        @param image PIL image
        @param size resize image size
        @return resized cropped and resized image
        """
        crop_rect = self._random_crop_rect(image.size)
        cropped = image.crop(crop_rect)
        resized = image.resize(size, Image.BILINEAR)

        return resized


    def crop(self):
        """
        if you want to crop negative dataset, you use this public method
        """
        negative_list = self._list_negative()

        # make negative cropped image list file
        with open(self._LST_NAME, 'w') as fout:
            fout.write('')

        for negative_name in negative_list:
            image = Image.open(negative_name)
            resized = self._crop_and_resize_image(image)
            resized_negative_name = negative_name.replace('/neg/', '/neg_cropped/')

            with open(self._LST_NAME, 'a') as fout:
                fout.write(resized_negative_name + '\n')

            if negative_name.endswith('.png'):
                resized.save(resized_negative_name, 'PNG')
            elif negative_name.endswith('.jpg'):
                resized.save(resized_negative_name, 'JPEG')
            else:
                resized.save(resized_negative_name, 'PNG')