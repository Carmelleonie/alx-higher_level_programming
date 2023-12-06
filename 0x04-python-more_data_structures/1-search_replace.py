#!/usr/bin/python3
def search_replace(my_list, search, replace):
   my_new = [replace if i == search else i for i in my_list]
   return my_new
