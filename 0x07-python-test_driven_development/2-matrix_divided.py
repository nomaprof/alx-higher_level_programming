#!/usr/bin/python3

"""Create a matrix for mathematical computation"""


def matrix_divided(matrix, div):
    """All elements of the matrix are divided

    Args:
        matrix (list): the matrix is a list of lists of int or float
        div (int/float): the dividing parameter
    Raises:
        TypeError: If the matrix contains any input apart from ints and floats
        TypeError: If the matrix contains rows of varying sizes
        TypeError: If div is not an int or float.
        ZeroDivisionError: If the divisor is 0
    Returns:
      A modified matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
