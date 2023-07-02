#!/usr/bin/python3
"""Square class to draw a square with coordinates"""


class Square():
    """square class with only positive integers as arguments"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize all data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size"""
        return self.__size

    @property
    def position(self):
        """get position"""
        return self.__position

    @size.setter
    def size(self, value):
        """set size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """set the positon"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """find the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print the defind square"""
        if self.size == 0:
            print()
        else:
            for m in range(self.position[1]):
                print("")
            for m in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
