#!/usr/bin/python3
"""Working on object oriented programming with python"""


class Square():
    """Class that represents a square"""

    def __init__(self, size):
        """initialize the square class

        Args:
            size (int): a private instance of the size of the square
        """
        self.__size = size
