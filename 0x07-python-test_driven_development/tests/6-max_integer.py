#!/usr/bin/python3
"""Get the maximum integer of a list
"""

def max_integer(list=[]):
    """get the maximum integer from a list but return none if empty"""
    if len(list) == 0:
        return None
    result = list[0]
    m = 1
    while m < len(list):
        if list[m] > result:
            result = list[m]
        m += 1
    return result
