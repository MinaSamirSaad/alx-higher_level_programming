#!/usr/bin/python3
"""
Print a square module

This module prints a square with the character # taking the size to print.
Otherwise raise a TypeError or ValueError exception with custom error messages.

"""


def print_square(size):
    """
    Arguments:
    @size: size of the square

    Returns:
    Nothing; only prints the square, otherwise raise a TypeError or ValueError
    when size is not an integer or if size is less than 0, respectively

    Example:
    >>> print_square(4)
    ####
    ####
    ####
    ####
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for _ in range(size):
        print('#' * size)
