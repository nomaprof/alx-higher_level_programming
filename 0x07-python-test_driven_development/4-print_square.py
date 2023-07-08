#!/usr/bin/python3
"""Print as square using this function"""


def print_square(size):
    """ create the square
        Arguments:
            @size: the size wanted by the user
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
