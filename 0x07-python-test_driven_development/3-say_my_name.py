#!/usr/bin/python3
"""Print the first and last name to the user"""


def say_my_name(first_name, last_name=""):
    """ give the first name and last name of user
        Arguments:
            @first_name: first name of the user
            @last_name: last name of the user
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
