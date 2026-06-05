#!/usr/bin/python3
"""Module that contains matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(error)

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(error)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(item / div, 2) for item in row]
        for row in matrix
    ]
