#!/usr/bin/python3
for i in range(99):
    if (i < 10):
        i = f"0{i}"
    print("{}".format(i), end=', ')
print("{}".format(99))
