#!/usr/bin/python3

"""Create a function that converts json to object"""
import json


def from_json_string(my_str):
    """Return the object from a json file"""
    return json.loads(my_str)
