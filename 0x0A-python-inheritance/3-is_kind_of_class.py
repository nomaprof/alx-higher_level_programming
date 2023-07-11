#!/usr/bin/python3

"""Check to see if object is an instance of a class or a base class"""


def is_kind_of_class(obj, a_class):
    """Determine if an object is an instance of a class or a base class

    Args:
        obj (any): The object
        a_class (type): The class used to match object.
    Returns:
        If the object is truly an instance of the class or a base class - True.
        Contrarywise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
