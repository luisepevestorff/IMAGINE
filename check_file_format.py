#!/usr/bin/env python

import os

def file_format(path):
    name, format  = os.path.splitext(path)
    return (format)

path_to_file = "/Users/luise/Pictures/Logos/Logo2.png"
format = file_format(path_to_file)

print(format)
print(format.lower())
format_lowercase = format.lower() 
if format_lowercase != ".jpg" or format_lowercase != ".png" or format_lowercase != ".tif":
    print("Unsupported file format!")
else:
    print("All is well!")