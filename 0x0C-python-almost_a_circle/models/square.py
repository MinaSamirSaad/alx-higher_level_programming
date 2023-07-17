#!/usr/bin/python3
""" Rectangle module 0-rectangle.py creates rectangle class """
from .rectangle import Rectangle


class Square(Rectangle):
    ''' Square class sublass of Rectangle class '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Square constructor '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' update attributes with values in args or kwargs'''
        try:
            if (args and len(args)):
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            elif (kwargs and len(kwargs)):
                for k, v in kwargs.items():
                    if hasattr(self, k):
                        setattr(self, k, v)
        except Exception:
            pass

    def __str__(self):
        ''' string represent the object '''
        # [Square] (id) x/y - width/height
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id, self.x, self.y,
            self.width
        )

    def to_dictionary(self):
        """Returns dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
