#!/usr/bin/python3

"""Checks if an object belongs to an instance of a certain class"""


def is_same_class(obj, a_class):
    """Confirm that an object is an instance of a given class
    and return true or false"""
    return (type(obj) == a_class)
