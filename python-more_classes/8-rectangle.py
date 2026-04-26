#!/usr/bin/python3
"""
This module defines a Rectangle class with a static method
to compare rectangles based on area.
"""


class Rectangle:
    """A class that defines a rectangle."""

    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle and increments the counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on area.
        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.
        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Returns a string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        line = str(self.print_symbol) * self.__width
        rect_lines = [line for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns a string representation to recreate the instance."""
        return "Rectangle({:d}, {:d})
