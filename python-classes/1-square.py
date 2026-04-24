#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize the square with a specific size.

        Args:
            size: The size of the square's side.
        """
        self.__size = size
