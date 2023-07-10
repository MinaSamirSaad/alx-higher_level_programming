#!/usr/bin/python3
"""
Add an attribute if it can
"""


def add_attribute(obj, attr_name, attr_value):
    """ add attributes """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
