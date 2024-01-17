import imageio.v2 as imageio
import re
from PIL import Image
import os
from check_file_format import FileFormat

print("Welcome to IMAGINE - the single edition , your frienly package to display all the information you ever wanted to know about your favourite image!")
image_name = input("Please type in what image you want to know everything about. ")

current_directory = os.getcwd()
path = current_directory+ "/" + image_name
format = FileFormat.file_format(path)

if format != ".jpg" and format != ".tif":
    raise ValueError("Hello World, this file format is not yet supported (we're working on that). Please choose a JPG or TIF file.")
else:
    image = imageio.imread(path)
    attributes = Image.open(path)

    width = attributes.width
    height = attributes.height
    megapixels = round((width*height/1000000))
    depth = re.sub(r'[a-z]', '', str(image.dtype))
    channels = len(Image.Image.getbands(attributes))

    def aspectRatio(w, h):
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

    print("You chose " + image_name + "! Here is all I know about your chosen file:" )
    print('Format: ', format)
    print('Width: ', width)
    print('Height: ', height)
    print('Bit Depth per Channel: ', depth)
    print('Bit Depth per Pixel: ', int(depth)*int(channels))
    print('Number of Channels: ', channels)
    print('Aspect Ratio: ', aspectRatio(width, height))
    print('Aspect Ratio rounded: ', aspectRatioRounded(width, height))
    print('Megapixels: ', megapixels)
    print('Mode: ', attributes.mode)
