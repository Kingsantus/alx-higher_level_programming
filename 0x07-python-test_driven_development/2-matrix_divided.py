#!/usr/bin/python3
"""
matrix_divided() module
this module loop through a list ensure it an int or float
it divides every element in the list by the second argument
return a new list of the result of element / div
"""
def matrix_divided(matrix, div):
    """
    accepts two argument
    Args 1: a list that is all int or float
    Args 2: an int or list
    """
    for row in matrix:
        """
        interate through Args 1 and ensure it all int
        if not an int or float
        Raise: TypeError
        """
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    """
    row_size is a var that handle the result of len(Args 1)
    """
    if any(len(row) != row_size for row in matrix):
        """
        if Args 1 is more than 1 list, loop through it to ensure
        every list is equal in length
        if not of equal length
        Raise: TypeError
        """
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        """
        Args 2 must be an int or float
        if not
        Raise: TypeError
        """
        raise TypeError("div must be a number")
    if div == 0:
        """
        Args 2 must not be 0
        as 0 is not a valid means of division
        Raise: ZeroDivisionError
        """
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        """
        if the condition is meet
        Args 1 / Args 2
        Result: will be stored in a new list
        the new list is returned
        """
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return (divided_matrix)
