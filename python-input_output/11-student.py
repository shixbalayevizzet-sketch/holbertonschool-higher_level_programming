#!/usr/bin/python3
"""
This module defines a Student class with JSON save and reload functionality.
"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance using a dict."""
        for key, value in json.items():
            setattr(self, key, value)
