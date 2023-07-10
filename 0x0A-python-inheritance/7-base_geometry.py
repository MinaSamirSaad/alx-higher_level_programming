#!/usr/bin/python3
"""
BaseGeometry module
"""


class BaseGeometry():
    """ Class BaseGeometry """

    def area(self):
        """ Public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method validator
        Check the value
        Arguments:
        @name: is always a string
        @value: value to check
        Return:
        raise a TypeError exception if value is not an integer
        raise a ValueError exception if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
