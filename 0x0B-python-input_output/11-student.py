#!/usr/bin/python3

"""Create a student class"""


class Student:
    """Define the student class"""

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

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student class

        Args:
            attrs (list): (Optional) The attributes
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student class

        Args:
            json (dict): The key/value pairs
        """
        for k, v in json.items():
            setattr(self, k, v)
