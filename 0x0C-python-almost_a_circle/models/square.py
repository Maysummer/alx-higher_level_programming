#!/usr/bin/python3
"""class that inherits for base class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiate object"""
        self.size = size
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """overload str method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method of variable arguments"""
        if (args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.size = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
