#!/usr/bin/python3
def print_last_digit(number):
	for i in number:
		n = ord(i)
		if n >= 97 and n < 123:
			num = chr(n - 32)
		else:
			num = i
			
		print("{}".format(num), end="")
	print()
