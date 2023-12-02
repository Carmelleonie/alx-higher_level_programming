#!/usr/bin/python3
def max_integer(my_list=[]):
    for idx in range(len(my_list) - 1):
        if not my_list:
            return None
        else:
            my_list.sort()
            return my_list[-1]
