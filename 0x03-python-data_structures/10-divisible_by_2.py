#!/usr/bin/python3
def divisible_by_2(my_list=[]):
	ne_li = []
	for i in my_list:
		if (i % 2) == 0:
			ne_li.append(True)
		else:
			ne_li.append(False)
	return ne_li 
