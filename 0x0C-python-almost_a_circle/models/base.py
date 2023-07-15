#!/usr/bin/python3
"""Class Base"""


class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialize instance"""
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = id
