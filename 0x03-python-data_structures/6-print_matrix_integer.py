#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """a function for printing matrices"""
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if n != 0:
                print(" ", end='')
            print("{:d}".format(matrix[m][n]), end='')
        print()
