#!/usr/bin/python3
from hidden_4 import *
names = dir(hidden_4)
if __name__ == "__main__":
    for i in names:
        if i[0] != '_':
            print("{}".format(i))
