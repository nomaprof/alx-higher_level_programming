#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    ans = [score * weight for (score, weight) in my_list]
    return sum(ans) / sum([weight for (score, weight) in my_list])
