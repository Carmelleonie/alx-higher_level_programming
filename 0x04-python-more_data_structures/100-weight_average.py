#!/usr/bin/pyhton3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    mark = 0
    coef = 0
    for i in my_list:
        mark += (i[0] * i[1])
        coef += i[1]
    return mark / coef
