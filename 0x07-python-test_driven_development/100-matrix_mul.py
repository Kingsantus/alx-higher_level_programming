#!/usr/bin/python3
"""matrix_mul module multiply element of two list 
return a new list"""

def matrix_mul(m_a, m_b):
    """matrix_mul multiply argument list provided"""
    if not isinstance(m_a, list):
        """Validate if m_a is a list"""
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        """Validate if m_b is a list"""
        raise TypeError("m_b must be a list")

    if any(not isinstance(row, list) for row in m_a):
        """Validate if m_a is a list of lists"""
        raise TypeError("m_a must be a list of lists")

    if any(not isinstance(row, list) for row in m_b):
        """Validate if m_b is a list of lists"""
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        """Validate if m_a is not empty"""
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        """Validate if m_b is not empty"""
        raise ValueError("m_b can't be empty")

    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        """Validate if m_a contains only integers or floats"""
        raise TypeError("m_a should contain only integers or floats")

    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        """Validate if m_b contains only integers or floats"""
        raise TypeError("m_b should contain only integers or floats")

    a_num_columns = len(m_a[0])
    """Validate if m_a and m_b are rectangles"""
    if any(len(row) != a_num_columns for row in m_a):
        raise ValueError("each row of m_a must be of the same size")

    b_num_columns = len(m_b[0])
    if any(len(row) != b_num_columns for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    if a_num_columns != b_num_columns:
        """Validate if m_a and m_b can be multiplied"""
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    """Perform matrix multiplication"""
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return (result)
