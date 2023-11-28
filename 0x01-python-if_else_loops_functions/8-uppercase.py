#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if n >= 97 and n < 123:	
            num = chr(n - 32)
        else:
            num = i	
        print("{}".format(num), end="")
    print("\n")
