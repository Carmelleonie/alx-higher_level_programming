#!/usr/bin/python3
def no_c(my_string):
	char_cC = "cC"
	my_ne = ""
	for char in my_string:
		if char not in char_cC:
			my_ne = my_ne + char
	return my_ne
