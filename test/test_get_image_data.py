import pytest
from IMAGINE.get_image_data import JpgTif
import imageio.v2 as imageio
from PIL import Image

testpath_1 = './testfile_jpg.jpg'

def test_width():
    image_test = imageio.imread(testpath_1)
    attributes_test = Image.open(testpath_1)
    testwidth = JpgTif(attributes_test, image_test)
    width = testwidth.width()
    assert width == 20

def test_height():
    image_test = imageio.imread(testpath_1)
    attributes_test = Image.open(testpath_1)
    testheight = JpgTif(attributes_test, image_test)
    height = testheight.height()
    assert height == 20

def test_megapixels():
    image_test = imageio.imread(testpath_1)
    attributes_test = Image.open(testpath_1)
    image_test = imageio.imread(testpath_1)
    attributes_test = Image.open(testpath_1)
    testpixel = JpgTif(attributes_test, image_test)
    megapix = testpixel.megapixels()
    assert megapix == 0

def test_aspectRatio():
    image_test = imageio.imread(testpath_1)
    attributes_test = Image.open(testpath_1)
    testRatio = JpgTif(attributes_test, image_test)
    ratio = testRatio.aspectRatio()
    assert ratio == (1, 1)

def test_aspectRatioRounded():
    image_test = imageio.imread(testpath_1)
    attributes_test = Image.open(testpath_1)
    testRatioRounded = JpgTif(attributes_test, image_test)
    ratioRounded = testRatioRounded.aspectRatioRounded()
    assert ratioRounded == (1, 1)

