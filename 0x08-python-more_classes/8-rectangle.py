#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """ This is Rectangle Class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialzie Rectangle Class
        Arguments:
        @width: width of the rectangle
        @height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Define rectangle string """
        string = ""
        if self.__height == 0 or self.width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i < (self.__height - 1):
                string += '\n'
        return string

    def __repr__(self):
        """Define rectangle representation"""
        return ("Rectangle({}, {})".format(
            eval(str(self.width)), eval(str(self.height))))

    def __del__(self):
        """ Print a message when an instance is deleted  """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """ Calculates the area of the rectangle
        Returns:
        The area of the rectangle
        """
        return ((self.__width) * (self.__height))

    def perimeter(self):
        """ Calculates the perimeter of the rectangle
        Returns:
        The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (((self.__width) + (self.__height)) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Check the biggest rectangle based on the area
        Arguments:
        @rect_1: first rectangle, must be an instance of Rectangle
        @rect_2: second rectangle, must be an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
