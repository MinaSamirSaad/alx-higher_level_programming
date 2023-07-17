#!/usr/bin/python3
""" Rectangle module 0-rectangle.py creates rectangle class """
from .base import Base


class Rectangle(Base):
    ''' Rectangle class sublass of Base class

        Attributes:
            private instance width (int) : width or ractangle
            private instance height (int) : height of ractangle
            private instance x (int) : x position
            private instance y (int) : y position
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @width.setter
    def width(self, value):
        ''' width setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        ''' height setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        ''' x setter '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        ''' y setter '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def update(self, *args, **kwargs):
        ''' update attributes with values in args if exits or kwargs'''
        try:
            if (args and len(args)):
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            elif (kwargs and len(kwargs)):
                for k, v in kwargs.items():
                    if hasattr(self, k):
                        setattr(self, k, v)
        except Exception:
            pass

    def area(self):
        ''' return area of rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' draw rectangle with symbol #'''
        print('\n'*self.y, end='')
        for i in range(self.height):
            print(" "*self.x, end='')
            print("#"*self.width)

    def __str__(self):
        ''' string represent the object '''
        # [Rectangle] (id) x/y - width/height
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id, self.x, self.y,
            self.width, self.height
        )

    def to_dictionary(self):
        """Returns dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
