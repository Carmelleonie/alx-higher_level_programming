#!/usr/bin/python3
j = 0
for i in range(122, 96, -1):
    print("{}".format(chr(i - j)), end="")
    j = 32 if j == 0 else 0
