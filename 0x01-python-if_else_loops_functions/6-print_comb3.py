#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if ((i == j) or (j < i)):
            continue
        elif ((i != 8) or (j != 9)):
            print("{}{}, ".format(i, j), end='')
        else:
            print ("{}{}".format(i,j))
