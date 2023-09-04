#!/usr/bin/python3

class Rectangle:

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initialize class
	    Args:
		width(int): width of rectangle
		height(int): height of rectangle
	"""
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

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
        """ Set height"""
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
        return "\n".join([str(Rectangle.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compare two rectangles and return the bigger or equal one"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

