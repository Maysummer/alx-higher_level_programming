#!/usr/bin/python3
"""define a square"""


class Square:
    """defines a square with optional attribute
    Attribute:
        size(int): square size.
    """
    def __init__(self, size=0):
        """instantiate the data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        self.__size = size

    def area(self):
        """returns current square area"""
        return self.__size ** 2
