#!/usr/bin/python3
''' module 0-saqure.py creates square class '''


class Square:
    ''' sqaure class doc '''
    def __init__(self, size=0):
        ''' constructor doc '''
        if not isinstance(size, int):
            raise TypeError("size must be an intege")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
