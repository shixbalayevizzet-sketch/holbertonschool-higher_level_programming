#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """A class that defines a square by size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): The size of the square's side.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position attribute with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # considering its position."""
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan boşluq (position[1])
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")

        # Kvadratın sətirləri
        for _ in range(self.__size):
            # Soldan boşluq (position[0])
            print(" " * self.__position[0] + "#" * self.__size)
