#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    arg = len(sys.argv) - 1

    if arg > 0:
        for i in range(arg):
            res += int(sys.argv[i + 1])	
    print("{:d}".format(res))
