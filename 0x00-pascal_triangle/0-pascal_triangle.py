#!/usr/bin/python3
"""
Create a function def pascal_triangle(n)
Returns a list of lists of integers
representing the Pascal's triangle of (n)

Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    """
    return empty list if n <= 0
    """
    if n <= 0:
        return []

    a = [[] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    a[i].append(1)
                else:
                    a[i].append(a[i - 1][j] + a[i - 1][j - 1])
            elif (j == i):
                a[i].append(1)
    return a
