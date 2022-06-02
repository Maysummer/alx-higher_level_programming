#!/usr/bin/python3
import sys
arg = sys.argv
length = len(arg)
j = 0
if __name__ == "__main__":
    for i in range(1, length):
        j += int(arg[i])
    print(j)
