#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newlist = []
    for i in set_1:
        for j in set_2:
            if i is not j:
                newlist.append(i)
    return newlist
