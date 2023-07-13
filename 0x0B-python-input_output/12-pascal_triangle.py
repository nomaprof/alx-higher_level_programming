#!/usr/bin/python3

"""Create a function for writing the Pascal Triangle"""


def pascal_triangle(n):
    """Define the Pascal triangle of size n.

    Returns a list of lists of integers that forms the Pascal triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trian = triangles[-1]
        temp = [1]
        for m in range(len(trian) - 1):
            temp.append(trian[m] + trian[m + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
