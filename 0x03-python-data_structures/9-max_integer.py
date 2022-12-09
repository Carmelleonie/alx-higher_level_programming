#!/usr/bin/python3
def max_integer(my_list=[]):
	for idx in range(len(my_list) - 1):
		if my_list == []:
			return None
		else:
			if my_list[idx] < my_list[idx + 1]:
				return my_list[idx + 1]
			else:
				return my_list[idx]
