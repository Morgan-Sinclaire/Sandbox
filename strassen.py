import math
import numpy as np

def naive(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    m,n = C.shape
    d = A.shape[1]
    for i in range(m):
        for j in range(n):
            C[i,j] = sum([A[i,k] * B[k,j] for k in range(d)])
    return C


def strassen(A, B):
    n = A.shape[0]
    p = math.log2(n)
    if p % 1 > 0:
        dim = 2**(int(p)+1)
        temp = np.zeros((n, dim - n))
        A = np.concatenate((A, temp), axis=1)
        B = np.concatenate((B, temp), axis=1)
        temp = np.zeros((dim - n, dim))
        A = np.concatenate((A, temp), axis=0)
        B = np.concatenate((B, temp), axis=0)

    return strassen2(A,B)[:n,:n]


def strassen2(A, B):
    if A.shape[0] == 1:
        return A*B

    n = A.shape[0]
    h = n // 2
    A1,A2,A3,A4 = A[:h,:h], A[:h,h:], A[h:,:h], A[h:,h:]
    B1,B2,B3,B4 = B[:h,:h], B[:h,h:], B[h:,:h], B[h:,h:]

    m1 = strassen(A1 + A4, B1 + B4)
    m2 = strassen(A4 + A3, B1)
    m3 = strassen(A1, B2 - B4)
    m4 = strassen(A4, B3 - B1)
    m5 = strassen(A1 + A2, B4)
    m6 = strassen(A3 - A1, B1 + B2)
    m7 = strassen(A2 - A4, B3 + B4)

    C = np.zeros((n,n))
    C[:h,:h], C[:h,h:], C[h:,:h], C[h:,h:] = \
        [m1 + m4 - m5 + m7, m3 + m5, m2 + m4, m1 - m2 + m3 + m6]
    return C

# n = 100
# A = np.random.randint(10, size=(n,n))
# B = np.random.randint(10, size=(n,n))
# %timeit naive(A,B)
# %timeit strassen(A,B)
