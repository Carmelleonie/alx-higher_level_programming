#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            if type(my_list) is int:
                print("{}".format(my_list[i]), end="")
                n += 1
        except (ValueError, TypeError):
            continue
    print()
    return n
