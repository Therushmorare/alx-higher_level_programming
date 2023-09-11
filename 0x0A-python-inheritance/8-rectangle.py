#!/usr/bin/python3

""" base geo class """
class BaseGeometry:
    """ base geo class """
    def area(self):
    """ function area """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ integer validator
            Args:
                name (string): string to be entered
                value (int): integer to be validated
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" class rectrange that inherits base """
class Rectangle(BaseGeometry):
    """ class rectrange that inherits base geo """
    def __init__(self, width, height):
        """ initialize function
            Args:
                width (int): width of rec
                height (int): height of rec 
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ string formatter """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

