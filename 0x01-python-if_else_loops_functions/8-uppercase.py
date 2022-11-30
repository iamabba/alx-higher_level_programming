#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]):
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[i]) - num, end=''))
