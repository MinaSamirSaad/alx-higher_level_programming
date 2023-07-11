#!/usr/bin/python3
'''
function that creates an Object from a “JSON file”:
'''


import json


def load_from_json_file(filename):
    '''
    function that creates an Object from a “JSON file”:
    Arguments:
    @filename: the file that i will read the json data from it
    '''
    with open(filename, encoding='utf-8') as f:
        return  json.load(f)
