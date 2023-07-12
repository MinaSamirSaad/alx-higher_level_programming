#!/usr/bin/python3
"""
function that inserts a line of text to a file, after each line containing a specific string 
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file, after each line containing a specific string
    """
    with open(filename, 'r+') as f:
        paragraph = f.readlines()
        f.seek(0, 0)
        for line in paragraph:
            f.write(line)
            if line.find(search_string) != -1:
                f.write(new_string)
