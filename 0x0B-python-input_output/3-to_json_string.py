#!/usr/bin/python3

"""Create a function that converts strings to JSON"""
import json


def to_json_string(my_obj):
    """Return the json format for an input string"""
    return json.dumps(my_obj)
