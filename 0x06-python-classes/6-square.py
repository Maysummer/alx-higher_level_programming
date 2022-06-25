#!/usr/bin/python3
"""defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """attr: Private instance attribute: size
        getter: retrieve data"""
        return self.__size

    @size.setter
    def size(self, value):
        """attr: Private instance attribute: size
        setter: set data"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """attr: Private instance attribute: position
        getter: retrieve data"""
        return self.__position

    @position.setter
    def position(self, value):
        """attr: Private instance attribute: position
        setter: set data"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 :
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return current square area"""
        return self.size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            for y in range(self.position[1]):
                print()
            for row in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print()
