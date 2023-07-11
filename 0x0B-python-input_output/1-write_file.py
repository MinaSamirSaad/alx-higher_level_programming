#!/usr/bin/python3
'''
function that writes a string to a text file (UTF8)
and returns the number of characters written
'''


def write_file(filename="", text=""):
    '''
    function that writes a string to a text file (UTF8)
    and returns the number of characters written
    Arguments:
    @filename: name of the file to write in
    @text: text to write in file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
