#!/usr/bin/python3
from functools import reduce
def best_score(a_dictionary):
    if type(a_dictionary) is not dict or len(a_dictionary) == 0:
        return None
    value = [a_dictionary[key] for key in a_dictionary]
    max_value = reduce(lambda a, b: a if (a > b) else b, value)
    for k, v in a_dictionary.items():
        if v == max_value:
            return k
