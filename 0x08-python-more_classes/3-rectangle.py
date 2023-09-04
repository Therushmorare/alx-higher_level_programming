#!/usr/bin/python3

""" class rectangle """
class Rectangle:
    """ initialize class
        Args:
             width (int): the width of rectangle
             height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

