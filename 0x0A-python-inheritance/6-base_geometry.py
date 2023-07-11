#!/usr/bin/python3

"""Create the  empty class called BaseGeometry."""


class BaseGeometry:
    """This is the created BaseGeometry class"""

    def area(self):
        """If this is not implemented, raise an exception"""
        raise Exception("area() is not implemented")
