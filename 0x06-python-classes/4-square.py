#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """instantiate the data
        Args:
            size(int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """get size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        return square area
        """
        return self.__size ** 2
