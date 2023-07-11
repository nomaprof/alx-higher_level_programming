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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
