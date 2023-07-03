#!/usr/bin/python3
"""create a square class"""


class Square:
    """The square class created"""

    def __init__(self, size=0, position=(0, 0)):
        """set initial value of square

        Args:
            size (int): what is the size of the square
            position (int, int): what is the cartesian coordinate of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the size of the square as needed"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the position of the square as needed"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the calculated or computed area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square using the # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for l in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for m in range(0, self.__position[0])]
            [print("#", end="") for n in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() function for getting the square shape to be printed to standard output"""
        if self.__size != 0:
            [print("") for l in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for m in range(0, self.__position[0])]
            [print("#", end="") for n in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
