#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = 0
    if my_list:
        for i in my_list:
            if len(my_list) == 0:
                return
            if i > max_num:
                max_num = i
        return max_num

