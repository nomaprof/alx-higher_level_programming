#!/usr/bin/python3

"""Create a function for writing to files"""


def write_file(filename="", text=""):
    """Write a string to a file in UTF8 format"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
