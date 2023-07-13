#!/usr/bin/python3

"""Creates a class to json converter function"""


def class_to_json(obj):
    """Return the dictionary representation of the data structure"""
    return obj.__dict__
