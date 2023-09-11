#!/usr/bin/python3

""" base geometry class """
class BaseGeometry:
    """ area function """
    def area(self):
        raise Exception("area() is not implemented")

    """ integer_validator function
        Args:
            name (string): name string
            value (int): int to be validated 
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
