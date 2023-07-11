#!/usr/bin/python3

"""Create a subclass called MyList"""

class MyList(list):
    """Sort the the content of the list and other contents available in MyList"""

    def print_sorted(self):
        """provide the list in ascending order"""
        print(sorted(self))
