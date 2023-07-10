#!/usr/bin/python3
"""
Function that verify if an object is a exactly an instance of the specified
class, if it's true return True, otherwise False
"""


def is_same_class(obj, a_class):
    """
    Arguments:
    @obj: object to verify
    @a_class: class of the object to verify
    Return:
    True if the object is exactly an instance of the class, otherwise False
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
