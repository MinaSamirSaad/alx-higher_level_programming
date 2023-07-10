#!/usr/bin/python3
'''
unction that returns True if the object is exactly an instance of the specified class 
otherwise False
'''


def is_same_class(obj, a_class):
    '''
    Arguments:
    obj: the object
    a_class: the class
    Return:
    True if the object is exactly an instance of the specified class 
    otherwise False
    '''
    if not obj or not a_class:
        return False
    return isinstance(obj, a_class)
