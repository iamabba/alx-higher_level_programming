#!/usr/bin/python3
for ch in range(97, 123):
    if ch != 113 and ch != 101:
        print("{:c}" .format(ch), end='')
