#!/usr/bin/python3
"""Square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square, inherits from Rectangle """
    def __init__(self, size):
        """ Instantiation with size
        @size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
