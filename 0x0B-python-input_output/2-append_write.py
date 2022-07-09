#!/usr/bin/python3
"""function that appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """append to file"""
    with open(filename, mode='a', encoding='UTF8') as f:
        return f.write(text)
