#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for row in new_matrix:
        for i in range(0, len(row)):
            row[i] *= row[i]
    return new_matrix
