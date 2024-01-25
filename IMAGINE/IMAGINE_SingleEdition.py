#!/usr/bin/python

import imageio.v2 as imageio
#import re
from PIL import Image
import os
from check_file_format import FileFormat
from get_exif_files import JpgTif

'''
def aspectRatio(w, h):
        """Aspect ratio calculation
        Calculate the aspect ratio of the image.

        Args:
            w (integer): the width of the image.
            h (integer): the height of the image.
        
        Returns:
            two integers: the aspect ratio of the image, width to height.
        """
        ratio = w/h
        if ratio.is_integer():
            resultA = w/100
            resultB = h/100
        else:
            for i in range(1,int(1e6)):
                r = i*ratio
                if r.is_integer():
                    resultA = i
                    resultB = int(r)
                    break
        return resultB, resultA

def aspectRatioRounded(w, h):
    """Aspect ratio calculation rounded
    Calculate the aspect ratio of the image rounded to the nearest integer.

    Args:
        w (integer): the width of the image.
        h (integer): the height of the image.
        
    Returns:
        two integers: the rounded aspect ratio of the image, width to height.
    """
    ratio = w/h
    if ratio.is_integer():
        resultA = w/100
        resultB = h/100
    else:
        for i in range(1,int(1e6)):
            r = round(i*ratio)
            if r.is_integer():
                resultA = i
                resultB = int(r)
                break
    return resultB, resultA
    '''

if __name__ == '__main__':
    print("Welcome to IMAGINE - the single edition , your frienly package to display all the information you ever wanted to know about your favourite image!")
    image_name = input("Please type in what image you want to know everything about. ")

    current_directory = os.getcwd()
    path = current_directory+ "/" + image_name
    format = FileFormat(path).file_format()

    
    image = imageio.imread(path)
    attributes = Image.open(path)

    data = JpgTif(attributes, image)

    print("You chose " + image_name + "! Here is all I know about your chosen file:" )
    print('Format: ', format)
    print('Width: ', data.width())
    print('Height: ', data.height())
    print('Bit Depth per Channel: ', data.depth())
    print('Number of Channels: ', data.channels())
    print('Bit Depth per Pixel: ', data.depth_per_pixel())
    print('Aspect Ratio: ', data.aspectRatio())
    print('Aspect Ratio rounded: ', data.aspectRatio())
    print('Megapixels: ', data.megapixels())
    print('Mode: ', data.colour_mode())