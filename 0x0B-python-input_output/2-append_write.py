#!/usr/bin/python3
'''
function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
'''


def append_write(filename="", text=""):
    '''
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Arguments:
    @filename: name of the file to append in
    @text: text to write in file
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
