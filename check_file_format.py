#!/usr/bin/env python

import os

class FileFormat:
    """Check for file format

    Args:
        path: the path to the desired file
    
    """
    def __init__(self, path):
        self.path = path

    def file_format(self):
        name, file_extension  = os.path.splitext(self.path)
        format_lower = file_extension.lower()
        return(format_lower)