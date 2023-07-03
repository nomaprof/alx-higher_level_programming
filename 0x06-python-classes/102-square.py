#!/usr/bin/python3
"""Create a class called square"""


class Square:
    """The class called square"""

    def __init__(self, size=0):
        """Set initial values of square

        Args:
            size (int): set the size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the present size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the computed or calculated area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == way to compare two squares"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != way of comparing two squares"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < way of comparing two squares"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= way of comparing two squares"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > way of comparing two squares"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= way of comparing two squares"""
        return self.area() >= other.area()
