#!/usr/bin/python3

"""Check to see if object is an instance of a class or a base class"""


def inherits_from(obj, a_class):
    """Determine if an object is an instance of a class or a base class

    Args:
        obj (any): The object
        a_class (type): The class used to match object.
    Returns:
        If the object is truly an instance of the class or a base class - True.
        Contrarywise - False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
