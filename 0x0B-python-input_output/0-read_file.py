#!/usr/bin/python3

"""Create a function for reading text in a file"""


def read_file(filename=""):
    """Print the text content of a file in UTF8 format"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
