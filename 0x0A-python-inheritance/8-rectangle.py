#!/usr/bin/python3

""" base geo class """
class BaseGeometry:
    """ function area """
    def area(self):
        raise Exception("area() is not implemented")
    """ integer validator
        Args:
            name (string): string to be entered
            value (int): integer to be validated
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" class rectrange that inherits base geo """
class Rectangle(BaseGeometry):
    """ initialize function
        Args:
            width (int): width of rec
            height (int): height of rec 
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """ string formatter """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

