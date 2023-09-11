#!/usr/bin/python3

""" BaseGeo class """
class BaseGeometry:
    """ area function """
    def area(self):
        raise Exception("area() is not implemented")

    """ integer validator
        Args:
            name (string): the string to be entered
            value (int): the int value to be entered
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
""" rec class """
class Rectangle(BaseGeometry):
    """ initialize funtion
        Args:
            width (int): the rec width
            height (int): the rec height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """ calculate the area of rec """
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

