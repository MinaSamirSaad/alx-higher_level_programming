#!/usr/bin/python3
''' module 0-saqure.py creates square class '''


class Square:
    ''' sqaure class doc '''
    def __init__(self, size=0):
        ''' constructor doc '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        ''' get size '''
        return self.__size

    @size.setter
    def size(self, size):
        ''' size setter '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' compute area of square '''
        return self.__size ** 2

    def __eq__(self, other):
        ''' compare with equal '''
        return (self.__size == other.size)

    def __ne__(self, other):
        ''' compare with not equal '''
        return (self.__size != other.size)

    def __ge__(self, other):
        ''' compare with greater equal '''
        return (self.__size >= other.size)

    def __le__(self, other):
        ''' compare with less equal '''
        return (self.__size <= other.size)

    def __gt__(self, other):
        ''' compare with greater '''
        return (self.__size > other.size)

    def __lt__(self, other):
        ''' compare with less '''
        return (self.__size < other.size)
