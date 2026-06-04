#!/usr/bin/python3
"""
Module 7-base_geometry
Contains class BaseGeometry
"""


class BaseGeometry:
    """
    A class used to represent Base Geometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception 
        with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value provided.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
