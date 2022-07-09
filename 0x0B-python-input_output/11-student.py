#!/usr/bin/python3
"""class Student that defines a student by"""


class Student:
    """class Student that defines a student by"""
    def __init__(self, first_name, last_name, age):
        """initialize object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_list = {}
        if attrs is None:
            return self.__dict__

        for elem in attrs:
            if elem in self.__dict__:
                new_list[elem] = self.__dict__[elem]
        return new_list

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
