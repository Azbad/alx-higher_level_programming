#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the division.
    """
    If (not isinstance(matrix, list)or not matrix or
            not all(isinstance(row, list) for row in matrix) or 
            not all(isinstance(ele, (int, float))
                for row in matrix for ele in row)):
        raise TypeError("matrix must be a matrix (list of liists) of "
                "integers/floats")

        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeERROR("Each row of the matrix must have the same size")

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        return[[round(x /div, 2) for x in row] for row in matrix]
