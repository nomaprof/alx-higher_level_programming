#!/usr/bin/python3

"""Define a class called MagicClass to mimic a python bytecode"""

import math


class MagicClass:
    """create a circle class"""

    def __init__(self, radius=0):
        """Set the initial values of the circle

        Arg:
            radius (float or int): get radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the calculated or computed area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the calculated or computed circumfrence of the circle"""
        return (2 * math.pi * self.__radius)
