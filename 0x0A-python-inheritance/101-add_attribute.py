#!/usr/bin/python3

"""Create a function that adds attributes to objects in a class"""


def add_attribute(obj, att, value):
    """Try and add new attribute to an object 

    Args:
        obj (any): The object to an attribute is to be added
        att (str): The name of the attribute to add to the object
        value (any): The value of the attribute
    Raises:
        TypeError: If the attribute cannot te included
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
