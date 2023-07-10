#!/usr/bin/python3
'''
unction that returns True if the object is exactly an instance of the specified class 
otherwise False
'''


def is_kind_of_class(obj, a_class):
    '''
    Arguments:
    obj: the object
    a_class: the class
    Return:
    True if the object is exactly an instance of the specified class 
    otherwise False
    '''
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
