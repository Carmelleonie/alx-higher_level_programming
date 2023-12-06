#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_t = [y for x in (set_1, set_2) for y in x]
    new_list = list(filter(lambda i: new_t.count(i) == 1, new_t))
    return new_list
