#!/usr/bin/python3

"""Create a subclass called Square that inherits attributes from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Create the square subclass"""

    def __init__(self, size):
        """Initialize the values of the square subclass

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
