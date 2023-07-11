#!/usr/bin/python3
'''
function that writes an Object to a text file, using a JSON representation
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    function that writes an Object to a text file, using a JSON representation
    Arguments:
    @my_obj: the object to convert to json
    @filename: the file that i will write the json data on it
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
