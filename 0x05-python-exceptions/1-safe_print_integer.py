#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        if value.isdigit():
            return True
        else:
            return False
    except TypeError:
        print("")
