#!/usr/bin/python3
"""pascal triangle function, returning
a list of lists of integers"""


def pascal_triangle(n):
    """pascal triangle"""
    big = []
    if n <= 0:
        return big
    else:
        for i in range(1, n+1):
            small = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    small.append(1)
                else:
                    small.append(prev[j] + prev[j - 1])
            prev = small
            big.append(small)
        return big
