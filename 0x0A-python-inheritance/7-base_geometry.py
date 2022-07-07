#!/usr/bin/python3
""" an empty class BaseGeometry"""


class BaseGeometry:
    """an empty class BaseGeometry"""
    def area(self):
        """pub instance method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))
