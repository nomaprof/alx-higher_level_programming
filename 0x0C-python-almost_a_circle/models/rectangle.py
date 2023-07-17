#!/usr/bin/python3
"""This is the rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """The rectangle class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize all the attributes assciated with the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # The getter functions
    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Get the x value"""
        return self.__x

    @property
    def y(self):
        """Get the y value"""
        return self.__y

    # The setter functions
    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Set the x-value"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y-value"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """calculate the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Draws the rectangle using #"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Design a customized format for string representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """let every attribute be an argument"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Display the dictionary form` of a Rectangle"""

        obj_dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}

        return obj_dictionary
