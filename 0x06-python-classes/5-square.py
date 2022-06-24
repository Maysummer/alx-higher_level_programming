#!/usr/bin/python3
"""defines a square"""

class Square:
    """define a square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    @property
    def size(self):
        """attr: private instance atrribute size
        getter: retrieve data"""
        return self.__size

    @size.setter
    def size(self, value):
        """attr:  private instance atrribute size
        setter: set data"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """current square area"""
        return self.size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
