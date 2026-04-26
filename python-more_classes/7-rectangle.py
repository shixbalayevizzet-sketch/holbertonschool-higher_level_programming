#!/usr/bin/python3
"""
This module defines a Rectangle class with custom print symbols
and instance tracking.
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

    def __str__(self):
        """Returns a string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        # print_symbol-i string-ə çevirib sətirləri yaradırıq
        line = str(self.print_symbol) * self.__width
        rect_lines = [line for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns a string representation to recreate the instance."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message and decrements the counter upon deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
