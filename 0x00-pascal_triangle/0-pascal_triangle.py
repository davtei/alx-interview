#!/usr/bin/env python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal's triangle
        of n
    """
    if n <= 0:                  # if n is negative or 0
        return []               # return empty list
    triangle = [[1]]            # initialize triangle with 1
    for i in range(1, n):       # for each row
        row = [1]               # initialize row with 1
        for j in range(1, i):   # for each element in row
            # append sum of previous row's j and j-1 elements
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)           # append 1 to row
        triangle.append(row)    # append row to triangle
    return triangle             # return triangle
