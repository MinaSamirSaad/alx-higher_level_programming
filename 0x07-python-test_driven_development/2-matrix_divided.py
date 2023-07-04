#!/usr/bin/python3
"""
Divide a matrix module

This module divides all elements of a matrix.
Otherwise raise a TypeError exception or ZeroDivisionError exception
with custom error messages

"""


def matrix_divided(matrix, div):
    """
    Arguments:
    @matrix: must be a list of lists of integers or floats
    @div: must be a number (integer or float)

    Returns:
    A new matrix with all elements of matrix divided by div.
    Otherwise raise a TypeError exception if in matrix are not
    integers or floats, or ZeroDivisionError exception when an element
    is divided by 0.
    The result of division must be rounded to 2 decimal places.

    """
    te = "matrix must be a matrix (list of lists) of integers/floats"
    le = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(te)
    for element in matrix:
        if not isinstance(element, list):
            raise TypeError(te)
        for i in element:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(te)
            leng = len(matrix[0])
            if len(element) != leng:
                raise TypeError(le)
    if div ==  0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
