#!/usr/bin/python3
"""inherit class from task 7- base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inheritd from base geometry class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """compute area"""
        return self.__width * self.__height

    def __str__(self):
        """magic method to print rectangle"""
        return "[Rectangle] {}/{}".format(self.__width,  self.__height)
