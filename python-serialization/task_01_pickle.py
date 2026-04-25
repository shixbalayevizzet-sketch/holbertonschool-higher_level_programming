#!/usr/bin/env python3
"""
This module provides a class for serializing and deserializing
custom Python objects using the pickle module.
"""
import pickle


class CustomObject:
    """A custom class representing a person with serialization capabilities."""

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a structured format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, IOError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, OSError):
            return None
