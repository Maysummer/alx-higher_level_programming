#!/usr/bin/python3
import sys
arg = sys.argv
length = len(arg) - 1
if __name__ == "__main__":
    if (length == 0):
        print("{} arguments.".format(length))
    else:
        if (length == 1):
            print("{} argument:".format(length))
        else:
            print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, arg[i]))
