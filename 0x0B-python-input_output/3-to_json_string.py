#!/usr/bin/python3
'''
function that returns the JSON representation of an object (string):
'''

import json


def to_json_string(my_obj):
    '''
    function that returns the JSON representation of an object (string):
    Arguments:
    @my_obj: the object to convert to json
    '''
    return json.dumps(my_obj)
