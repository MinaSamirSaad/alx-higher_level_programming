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

    def area(self):
        """ Function that calculates the area of the rectangle
        Return:
        The area of the rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """ Returns the message to print """
        return ("[Rectangle] {:}/{:}".format(self.__width, self.__height))
