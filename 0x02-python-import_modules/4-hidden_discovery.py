#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
length = len(names)
if __name__ == "__main__":
    for i in range(1, length):
        print("{}".format(names[i]))
