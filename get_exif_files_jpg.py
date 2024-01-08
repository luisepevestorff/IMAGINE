import imageio.v2 as imageio
import re
from PIL import Image, ExifTags

path = #this is where the path is read in

image = imageio.imread(path)
type = Image.open(path)

megapixels = round((type.size[0]*type.size[1]/1000000))
d = re.sub(r'[a-z]', '', str(image.dtype))
t = len(Image.Image.getbands(type))
width = type.size[0]
height = type.size[1]

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

print('Format: ', type.format)
print('Width: ', width)
print('Height: ', height)
print('Bit Depth per Channel: ', d)
print('Bit Depth per Pixel: ', int(d)*int(t))
print('Number of Channels: ', t)
print('Aspect Ratio: ', aspectRatio(width, height))
print('Aspect Ratio rounded: ', aspectRatioRounded(width, height) )
print('Megapixels: ', megapixels)
print('Mode: ', type.mode)
