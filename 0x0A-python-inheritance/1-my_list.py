#!/usr/bin/python3

"""Create a class called MyList that inherits from the list class"""


class MyList(list):
    """The class that inherits from list"""

    def print_sorted(self):
        """print the list in ascending order"""
        print(sorted(self))
