#!/usr/bin/python3
""" class Student that defines a student"""


class Student:
    """ class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialize object"""
        first_name.self = first_name
        last_name.self = last_name
        age.self = age

    def to_json(self):
        """method to that retrieves a dictionary representation
        of a Student instance"""
        return self.__dict__
