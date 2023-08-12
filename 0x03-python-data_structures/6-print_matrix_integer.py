#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    col_num = len(matrix[0])

    for i in range(len(matrix)):
        for n in range(col_num):
            print("{:d}".format(matrix[i][n]), end="")
            if n < col_num - 1:
                print(" ", end="")
        print()
