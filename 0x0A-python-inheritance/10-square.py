#!/usr/bin/python3
"""class square thet inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        """magic method to print rectangle"""
        return "[Rectangle] {}/{}".format(self.__size,  self.__size)
