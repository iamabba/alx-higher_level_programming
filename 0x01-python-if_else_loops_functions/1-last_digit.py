#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    l_digits = number % 10
else:
    l_digits = number % -10

print("Last digit of {} is {}" .format(number, l_digits), end='')

if l_digits > 5:
    print(" and is greater than 5")
elif l_digits == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
