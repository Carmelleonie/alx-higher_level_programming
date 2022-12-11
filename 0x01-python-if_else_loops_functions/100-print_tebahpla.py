#!/usr/bin/python3
for i in range(122, 96, -1):
	lis = []
	if i % 2 != 0:
		char = chr(i - 32)
	else:
		char = chr(i)
	print(char, end="")
