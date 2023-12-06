#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = [k for k in a_dictionary]
    for i in sorted(key_list):
        print("{}: {}".format(i, a_dictionary[i]))
