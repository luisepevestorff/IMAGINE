from IMAGINE.check_file_format import FileFormat
import pytest

def test_file_format():
    testformat_1 = FileFormat('./testfile_jpg.jpg')
    extension_1 = testformat_1.file_format()
    
    testformat_2 = FileFormat('./testfile_tif.tif')
    extension_2 = testformat_2.file_format()
    
    assert extension_1 == '.jpg'
    assert extension_2 == '.tif'
    
    with pytest.raises(ValueError) as wrongformat:
        testformat_3 = FileFormat('./testfile_png.png')
        extension_3 = testformat_3.file_format()
    assert str(wrongformat.value) == "Hello World, this file format is not yet supported (we're working on that). Please choose a JPG or TIF file."