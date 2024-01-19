import imageio.v2 as imageio
import re
from PIL import Image, ExifTags
from check_file_format import FileFormat

class JpgTif:
    """A class to read the Exif data from a JPG file.

    Args:
    
    """

    #def __init__(self, path, w, h, attribute):
     #   self.path = path
      #  self.w = w
      #  self.h = h
       # self.attribute = attribute

    image = imageio.imread(path)
    attributes = Image.open(path)

    #width = attributes.width
    def width(attribute):
        image_width = attribute.width
        return image_width
    
    #height = attributes.height
    def height(attribute):
        image_heigth = attribute.height
        return image_height

    megapixels = round((width*height/1000000))
    depth = re.sub(r'[a-z]', '', str(image.dtype))
    channels = len(Image.Image.getbands(attributes))

    def aspectRatio(w, h):
        ratio = w/h
        if ratio.is_integer():
            resultA = w/100
            resultB = h/100
        else:
            for i in range(1,100):
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
            for i in range(1,100):
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
    print('Aspect Ratio rounded: ', aspectRatioRounded(width, height) )
    print('Megapixels: ', megapixels)
    print('Mode: ', attributes.mode)