#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """delete and index of a list"""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
