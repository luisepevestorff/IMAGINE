import os

print('Welcome to IMAGINE, your friedly local image search engine. \nThe parameters you can search for are: \nfile format, width, height, bit depth per channel, bit depth per pixel, number of channels, aspect ratio, megapixels and colour mode.')
print('Please specify what you want to search for by typing one of the following abbreviations: \nfile format: ff \nwidth: w \nheight: h \nbit depth per channel: bc \nbit depth per pixel: bp \naspect ratio: ar \nmegapixels: mp \ncolour mode: cm \n')
param = input('What do you want to search for? ').lower()
if param == 'ff' or param == 'w' or param == 'h' or param == 'bc' or param == 'bp' or param == 'ar' or param == 'mp' or param == 'cm':
    print('You selected ', param, '.')
    if param != 'ff' and param != 'cm':
        values = [int(values) for values in input('Please enter the integer value(s) you want to search for. ').split()]
        if values.is_integer():
            print('You entered the following value(s): ', values)
        else:
            print('Please enter only integers. If you want to search for a float number, please round up.')
    else:
        string = input('Please enter your search term. ')
        print('You entered: ', string)
else:
    print('Invalid input. Please try again and enter a valid abbreviation.')

#to do 1: put the other functions in here
#to do 2: split funtion integer testing not yet working