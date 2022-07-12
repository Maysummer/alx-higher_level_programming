#!/usr/bin/python3
"""class that inherits for base class"""


from models.rectangle import Rectangle


class Square(Rectangle):
      """square class"""
      def __init__(self, size, x=0, y=0, id=None):
          """instantiate object"""
          self.size = size
          super().__init__(id, x, y, width, height)
