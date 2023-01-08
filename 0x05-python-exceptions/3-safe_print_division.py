#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result:", a / b)
        return a / b
    except ZeroDivisionError:
        print("Inside result:", None)
        return None
