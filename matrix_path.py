"""
Given a matrix A, we want to find the path, traversing from left to right,
that has a maximal sum. The path must start on the first column, go left,
up, or down, never intersect with itself, and finish immediately upon
reaching the last column.
"""

import numpy as np

def max_col_sum(v, u, i):
    """
    Given a column v representing the actual entries of a matrix,
    a column u representing the maximum path sum getting to that entry,
    and a position i, return the max sum contiguous sequence terminating
    at index i.
    """
    # Initalize the list sequence with just the entry at i
    n = v[i]
    path = u[i]
    m = n + path
    # Check sequences starting below i
    for j in range(i+1, v.shape[0]):
        n += v[j]
        path = u[j]
        if n + path > m:
            m = n + path

    # Check sequences starting above i
    n = v[i]
    for j in range(i-1, -1, -1):
        n += v[j]
        path = u[j]
        if n + path > m:
            m = n + path

    return m


def max_path(A):
    """
    Find the maximal path in matrix A.
    """
    m,n = A.shape
    # create a matrix to store the max path sums seen so far
    B = np.zeros((m,n))

    # going column by column, set each entry to be the value of the
    # max path getting there, given the previous column
    for col in range(1, n):
        for row in range(m):
            B[row, col] = max_col_sum(A[:, col-1], B[:, col-1], row)

    # the last column must include the actual values reached at the end
    return np.max(B[:, -1] + A[:, -1])

# A = np.array([[-1, 8, 5], [8, 7, 4], [0, 4, 5]])
# print(max_path(A))
# A = np.array([[-100, 1, 10], [0, 0, 0], [0, 0, 5]])
# print(max_path(A))
