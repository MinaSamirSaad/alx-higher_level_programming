#!/usr/bin/python3
"""
Add Integer Module

This module takes two integers or/and float and adds them.
Otherwise raise a TypeError exception.
Floats must be casted into integers
"""


def add_integer(a, b=98):
    """
    Arguments:
    @a: First parameter
    @b: Second parameter, if is empty takes the value od 98

    Returns:
    An integer: a + b, otherwise raise a TypeError exception.

    Example:
    >>> add_integer(3, 2)
    5
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
