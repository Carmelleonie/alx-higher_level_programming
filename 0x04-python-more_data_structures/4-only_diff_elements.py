#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
	new_list = []
	for i in set_1:
		new_list.append(i)
	for j in new_list:
		for k in set_2:
			if j != k:
				new_list.append(k)
		return new_list
	
