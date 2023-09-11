#!/usr/bin/python3

""" base geometry class """
class BaseGeometry:
    """ base geometry class """
    def area(self):
        """ area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator function
            Args:
                name (string): name string
                value (int): int to be validated 
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
