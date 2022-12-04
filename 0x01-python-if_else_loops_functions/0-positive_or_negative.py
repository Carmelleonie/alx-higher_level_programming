#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
number = input('')
if number < 0:
    print(number + " is negative")
elif number > 0 and number != 0:
    print(number + " is positive")
elif number == 0:
    print(number + " is 0")
else:
    print("\n")