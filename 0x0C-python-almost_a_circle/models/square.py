#!/usr/bin/python3
"""
Class Square
"""

from .rectangle import Rectangle



class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__ (self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ Getter width """
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        try:
            if args:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            else:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self,key, value)
        except Exception:
            pass

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
