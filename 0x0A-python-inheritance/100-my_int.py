#!/usr/bin/python3

"""Create a class called MyInt that inherits attributes from int"""


class MyInt(int):
    """Invert the operators  == and !="""

    def __eq__(self, value):
        """Override == opeartor with != operator"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == operator"""
        return self.real == value
