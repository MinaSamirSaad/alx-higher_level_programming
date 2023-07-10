#!/usr/bin/python3
"""Rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        """ Instantiation with width and height
        Arguments:
        @width: size
        @height: size
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
