#!/usr/bin/python3
def search_replace(my_list, search, replace):
	for i in my_list:
		if i is search:
			return my_list.replace(search, replace)
