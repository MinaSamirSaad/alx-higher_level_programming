#!/usr/bin/python3
"""
Class Rectangle
"""
from .base import Base


class Rectangle(Base):
    """ This is Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for rectangle
        Arguments:
        @width: width of the rectangle
        @height: height of the rectangle
        @x: position in x
        @y: position in y
        @id: amount of instances created
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter of width
        Arguments:
        @value: value to set the width of the rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter of height
        Arguments:
        @value: value to set the height of the rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def validator(self, name, value):
        """
        validator - method that checks for legal values
        Arguments:
        @name: name of the attribute to check
        @value: value of the attribute to check
        Returns:
        A raise Type or Value error if is not an integer or
        if is not a positive number, respectly
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        self.validator("y", value)
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        self.validator("y", value)
        self.__y = value

    def area(self):
        """ Calculates the area of the rectangle
        Returns:
        The area of the rectangle
        """
        return ((self.width) * (self.height))

    def display(self):
        ''' the square with the character # '''
        for _ in range(self.y):
            print()
        if (self.height == 0 or self.width == 0):
            print()
        else:
            for _ in range(self.height):
                print(" " * self.x, end='')
                print('#' * self.width)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        try:
            if args:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            else:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self,key, value)
        except Exception:
            pass

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
