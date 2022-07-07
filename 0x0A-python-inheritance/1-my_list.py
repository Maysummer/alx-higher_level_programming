#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    def __init__(self):
        pass
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
