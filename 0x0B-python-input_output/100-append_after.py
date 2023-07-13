#!/usr/bin/python3

"""Create a function that inserts text into a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after a specific string is spotted in a file

    Args:
        filename (str): The file name
        search_string (str): The string to discover
        new_string (str): The string to insert into file
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
