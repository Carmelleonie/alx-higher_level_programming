#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new_max = []
	return[[col**2 for col in row] for row in matrix]
