#!/usr/bin/python3
"""Module that defines a Square class with getter and setter."""


class Square:
    """A class that defines a square with property and setter logic."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): The size of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the current square area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2
