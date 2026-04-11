#!/usr/bin/python3
"""
This module provides a function for integer addition.
It contains one function: add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number, must be an int or float.
        b: The second number, must be an int or float. Defaults to 98.

    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
