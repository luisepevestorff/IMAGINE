#!/usr/bin/env python

import os

path_to_file = "/Users/luise/Pictures/Logos/Logo2.png" #going to be based on input

def file_format(path):
    name, format  = os.path.splitext(path)
    return (format)

format = file_format(path_to_file) #to do: merge with line below
format_lowercase = format.lower()
if format_lowercase != ".jpg" and format_lowercase != ".png" and format_lowercase != ".tif":
    print("Unsupported file format!") #to do: add more formats?