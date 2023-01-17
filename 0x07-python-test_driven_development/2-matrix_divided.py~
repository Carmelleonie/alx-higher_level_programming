#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for item in matrix:
        if type(item) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i in item:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i+1]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in item] for item in matrix]
