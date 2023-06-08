#!/usr/bin/python3
def uppercase(str):
    for m in range(len(str)):
        if ord(str[m]) >= 97 and ord(str[m]) <= 122:
            value = 32
        else:
            value = 0
        print("{:c}".format(ord(str[m]) - value), end='')
    print()
