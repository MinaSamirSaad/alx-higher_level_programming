#!/usr/bin/python3
"""
Function that verify if an object is an instance of a class that
inherit(directly or indirectly) from the specified class, if the object is an
instance returns True, otherwisw False
"""


def inherits_from(obj, a_class):
    """
    Arguments:
    @obj: object to verify
    @a_class: class of the object to verify
    Return:
    True if the object is exactly an instance of the class, otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
