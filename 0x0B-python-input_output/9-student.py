#!/usr/bin/python3

"""Create a student class"""


class Student:
    """Create the student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student class

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student class"""
        return self.__dict__
