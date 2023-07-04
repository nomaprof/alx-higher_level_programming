#!/usr/bin/python3

"""Create a class callled Rectangle"""


class Rectangle:
    """Place other things about Rectangle class here"""

    def __init__(self, width=0, height=0):
        """Intialize the parameters of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width parameter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the answer for area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the answer for perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return a printed rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for m in range(self.__height):
            [rect.append('#') for n in range(self.__width)]
            if m != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
