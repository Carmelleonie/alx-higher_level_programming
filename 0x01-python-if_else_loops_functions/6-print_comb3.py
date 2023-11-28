#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i == 8 and j == 9 and i < j:
            print('{}{}'.format(i, j))
        elif i > j or i ==j:
            continue
        else:
            print('{}{},'.format(i, j), end=" ")
