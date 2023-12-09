#!/usr/bin/pyhton3
from functools import reduce
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    #tuple_2 = [tuple_t[1] for tuple_t in my_list]
    div = reduce(lambda a, b: a + b, list(map(lambda tuple_t: tuple_t[1], my_list)))
    result = reduce(lambda x, y: x + y, (list(map(lambda tuple_t: tuple_t[0] * tuple_t[1], my_list)))) / div
    return result
