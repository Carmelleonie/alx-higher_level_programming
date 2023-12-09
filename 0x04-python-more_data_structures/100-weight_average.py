#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    mark = 0; coef = 0
    for tuple_t in my_list:
        mark += (tuple_t[0] * tuple_t[1])
        coef += tuple_t[1]
    return mark / coef
