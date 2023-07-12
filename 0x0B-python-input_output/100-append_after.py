#!/usr/bin/python3
''' 100-append_after.py module'''


def append_after(filename="", search_string="", new_string=""):
    ''' inser new line with new_string
    after search_string found in current line'''
    with open(filename, 'r+') as f:
        paragraph = f.readlines()
        f.seek(0, 0)
        for line in paragraph:
            f.write(line)
            if line.find(search_string) != -1:
                f.write(new_string)
