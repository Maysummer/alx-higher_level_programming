#!/usr/bin/python3
from hidden_4 import *
names = dir(hidden_4)
length = len(names)
if __name__ == "__main__":
    for i in range(0, length):
        print("{}".format(names[i]))
