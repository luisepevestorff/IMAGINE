from IMAGINE.check_file_format import FileFormat
import pytest

def test_file_format():
    testformat = FileFormat('./testfile_jpg.jpg')
    extension = testformat.file_format()
    assert extension == '.jpg'

def test_file_format():
    testformat = FileFormat('./testfile_tif.tif')
    extension = testformat.file_format()
    assert extension == '.tif'

def test_file_format():
    with pytest.raises(ValueError) as wrongformat:
        testformat = FileFormat('./testfile_png.png')
        extension = testformat.file_format()
    assert str(wrongformat.value) == "Hello World, this file format is not yet supported (we're working on that). Please choose a JPG or TIF file."

def test_file_format():
    with pytest.raises(ValueError) as wrongformat:
        testformat = FileFormat('./__init__.py')
        extension = testformat.file_format()
    assert str(wrongformat.value) == "Hello World, this file format is not (yet) supported (we're working on that). Please choose a JPG or TIF file."