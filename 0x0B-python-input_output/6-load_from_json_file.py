#!/usr/bin/python3
'''
function that creates an Object from a “JSON file”:
'''

import json


def load_from_json_file(filename):
    '''
    function that creates an Object from a “JSON file”:
    Arguments:
    @filename: the file that i will write the json data on it
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        return  json.load(f)
