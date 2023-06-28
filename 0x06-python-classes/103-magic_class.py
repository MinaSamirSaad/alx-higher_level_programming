#!/usr/bin/python3
""" MagicClass module creates MagicClass class """


import math


class MagicClass:
    """ MagicClass class doc """
    def __init__(self, radius=0):
        ''' costructor of MagicClass '''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        ''' computes area of class as circle '''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        ''' computes circumference of class as circle '''
        return 2 * math.pi * self.__radius
