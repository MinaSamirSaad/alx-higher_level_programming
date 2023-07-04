#!/usr/bin/python3
"""
Say my name module

This module prints a full name.
Otherwise raise a TypeError exception with custom error messages.

"""


def say_my_name(first_name, last_name=""):
    """
    Arguments:
    @first_name: first name argument
    @last_name: last name argument, can be empty
    if it don'r receive a string

    Returns:
    Nothing; only prints the full name, otherwise raise a TypeError

    Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    """
    if not  isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
