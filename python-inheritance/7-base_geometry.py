#!/usr/bin/python3
"""Module 7-base_geometry
Contains class BaseGeometry
"""


class BaseGeometry:
    """A class used to represent Base Geometry."""

    def area(self):
        """Raises Exception: area() not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
