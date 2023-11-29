#!/usr/bin/env python

import os

def file_format(path):
    name, format  = os.path.splitext(path)
    return (format)

path_to_file = "/Users/luise/Pictures/Logos/Logo2.png"
format = file_format(path_to_file)
format_lowercase = format.lower()
if format_lowercase != ".jpg" and format_lowercase != ".png" and format_lowercase != ".tif":
    print("Unsupported file format!")

print(format)