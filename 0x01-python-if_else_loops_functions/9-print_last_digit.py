#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        value = number % 10
    else:
        value = number % -10
        value *= -1

    print("{:d}",format(value), end='')
    return (value)
