#!/usr/bin/python3

"""Create a function that appends an object to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """Write the object to the json file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
