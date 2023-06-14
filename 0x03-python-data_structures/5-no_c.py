#!/usr/bin/python3
def no_c(my_string):
    """Remove a character from a string"""
    ans = ""
    for m in range(len(my_string)):
        if my_string[m] != 'c' and my_string[m] != 'C':
            ans += my_string[m]
    return ans
