#!/usr/bin/python3
"""Module for the Rectangle class that inherits from BaseGeometry."""
from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A class that represents a Rectangle inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate inputs using the parent class method
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Set private attributes
        self.__width = width
        self.__height = height
