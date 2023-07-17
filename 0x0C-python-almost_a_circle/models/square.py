#!/usr/bin/python3
"""
Class Square
"""

from models.rectangle import Rectangle



class Square(Rectangle):
    """
    Square - class for a square, this class inherit form Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for square
        Arguments:
        @size: size of the rectangle
        @x: position in x
        @y: position in y
        @id: amount of instances created
        """
        super().__init__(size, size, x, y, id)

    def __str__ (self):
        """
        formats string representation of the Square
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ Getter width """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Setter for size of square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update - assign the arguments to each attribute
        @args: list of arguments
        @kargs: dictionary of arguments, key represents
        an attribute to the instance
        """
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
        """
        to_dictionary - returns a dictionary representation of a Square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
