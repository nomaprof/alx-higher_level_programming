#!/usr/bin/python3

"""Create a function for appending text to a file"""

def append_write(filename="", text=""):
    """Append a text to the end of a file in UTF8 format"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
