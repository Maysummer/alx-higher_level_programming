#!/usr/bin/python3
"""rectangle class that inherits from base class"""


from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve the width attribute"""
        return self.__width

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @property
    def x(self):
        """retrieves the x attribute"""
        return self.__x

    @property
    def y(self):
        """retrieves the y attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """set width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print in stdout the rectangle instance"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """override str method to return..."""
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """assigns a key/value argument to each attribute"""
        if len(args):
            for arg in args:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.__width = args[1]
                if len(args) >= 3:
                    self.__height = args[2]
                if len(args) >= 4:
                    self.__x = args[3]
                if len(args) >= 5:
                    self.__y = args[4]

        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "width":
                    self.__width = kwargs[key]
                if key == "height":
                    self.__height = kwargs[key]
                if key == "x":
                    self.__x = kwargs[key]
                if key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """returns dictionary representation of a rectangle"""
        dct = {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
        return dct

