#!/usr/bin/env python

import os

class FileFormat:
    """Check for file format

    Args:
        path: 
    
    """
    #def __init__(self, path):
        #self.path = path

    def file_format(path):
        name, file_extension  = os.path.splitext(path)
        format_lower = file_extension.lower()
        return(format_lower)
    
#path_to_file = "/Users/luise/Pictures/Logos/Logo2.png"
#format = file_format(path_to_file)
#format_lowercase = format.lower()
#if format_lowercase != ".jpg" and format_lowercase != ".png" and format_lowercase != ".tif":
#    print("Unsupported file format!")