#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """get members of list that are divisble by 2"""
    factors = []
    for m in range(len(my_list)):
        if my_list[m] % 2 == 0:
            factors.append(True)
        else:
            factors.append(False)
    return factors
