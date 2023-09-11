#!/usr/bin/python3

""" base geo class """
class BaseGeometry:
    """ area func """
    def area(self):
        raise Exception("area() is not implemented")
    """ integer validator
        Args:
            name (string): string to be use
            value (int): integer to be used
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" rec class """
class Rectangle(BaseGeometry):
    """ initialize class
        Args:
            width (int): width of rec 
            height (int): height of rec
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """ calculate area """
    def area(self):
        return self.__width * self.__height
    """ print rectanle """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

""" class square """
class Square(Rectangle):
    """ initialize class
        Args:
            size (int): size of rec
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
    """ print square """
    def __str__(self):
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

