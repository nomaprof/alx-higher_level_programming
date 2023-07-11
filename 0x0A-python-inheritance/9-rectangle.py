#!/usr/bin/python3

"""Create a class that inherits attributes from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Create the Rectangle class using attributes from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the values of the rectangle parameters

        Args:
            width (int): The width of the rectangle
            height (int): The heigth of the rectange
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the answer in the format specified below"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
