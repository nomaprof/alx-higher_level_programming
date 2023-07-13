#!/usr/bin/python3

"""Define a function that creates an object from a json file"""


def load_from_json_file(filename):
    """Create an object from a json file"""
    with open(filename) as f:
        return json.load(f)
