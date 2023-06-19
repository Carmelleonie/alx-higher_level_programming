#!/usr/bin/python3
"""A  a script that adds all arguments
to a Python list, and then save them to a file
"""
import sys

if __name__ == "__main__":
    """ This script adds all arguments to a Python list,
    and then save them to a file"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        list_arg = load_from_json_file("add_item.json")
    except:
        list_arg = []

    arg = len(sys.argv)
    if arg > 1:
        for i in range(1, arg):
            list_arg.append(sys.argv[i])
    save_to_json_file(list_arg, "add_item.json")

