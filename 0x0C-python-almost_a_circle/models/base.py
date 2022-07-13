#!/usr/bin/python3
""" base class"""


import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiate object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            my_str =  "[]"
        else:
            my_str = cls.to_json_string([item.to_dictionary() for item in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(my_str)
