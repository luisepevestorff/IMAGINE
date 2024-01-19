#!/usr/bin/env python

import os

class FileFormat:
    """Check for the file format of the image.

    Args:
        path (string): the path to the desired file.
    
    Returns: string: the file format of the image displayed in lower case letters.
    """
    def __init__(self, path):
        self.path = path

    def file_format(self):
        name, file_extension  = os.path.splitext(self.path)
        format_lower = file_extension.lower()
        return(format_lower)
#if format_lowercase != ".jpg" and format_lowercase != ".png" and format_lowercase != ".tif":
#print("Unsupported file format!")

