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
    
    def my_print(self):
        ''' the square with the character # '''
        if (self.__size == 0):
            print()
        for _ in range(self.__size):
            print('#' * self.__size)
