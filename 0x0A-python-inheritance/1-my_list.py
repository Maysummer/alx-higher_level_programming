#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = sorted(self)
        print(new_list)
