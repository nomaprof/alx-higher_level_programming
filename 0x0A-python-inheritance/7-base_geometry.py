#!/usr/bin/python3

"""Create the  empty class called BaseGeometry."""


class BaseGeometry:
    """This is the created BaseGeometry class"""

    def area(self):
        """If this is not implemented, raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Confirm that the parameter passed is an integer

        Args:
            name (str): The name of the parameter or variable
            value (int): The parameter or variable to check
        Raises:
            TypeError: when the value is anything other than an integer
            ValueError: when the value is  <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
