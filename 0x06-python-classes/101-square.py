#!/usr/bin/python3
''' module 0-saqure.py creates square class '''


class Square:
    ''' sqaure class doc '''
    def __init__(self, size=0, position=(0, 0)):
        ''' constructor doc '''
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' get size '''
        return self.__size

    @size.setter
    def size(self, size):
        ''' size settter '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        ''' get position '''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
                or any(not isinstance(n, int) for n in value) \
                or any(n < 0 for n in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        ''' compute area of square '''
        return self.__size ** 2

    def __str__(self):
        ''' replace __str__'''
        if (self.__size == 0):
            return ''
        square = ''
        square += '\n' * self.__position[1]
        for i in range(self.__size):
            square += ' ' * self.__position[0]
            square += '#' * self.__size
            if i + 1 < self.__size:
                square += '\n'
        return square
