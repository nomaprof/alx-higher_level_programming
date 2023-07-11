#!/usr/bin/python3

"""Checks if an object belongs to an instance of a certain class"""


def is_same_class(obj, a_class)
"""Confirm that an object is an instance of a given class
    
    Args:
        obj (any): the instance
        a_class (type): the class to match with object
    Returns:
        If object is an instance of the class - True.
        contrarywise - False.
    """
        if not isinstance(a_class, type):
        raise TypeError("a_class must be one type")
    return (type(obj) is a_class)
