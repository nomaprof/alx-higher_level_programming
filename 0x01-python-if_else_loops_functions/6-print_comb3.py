#!/usr/bin/python3
for value in range(0, 90):
    if value % 10 > value / 10:
        if value != 89:
            print("{:02d}, ".format(value), end='')
        else:
            print("{:02d}".format(value))
