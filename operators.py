"""
I found out that the operators m & n, m | n, and m ^ n act as a function on
integers m and n. At first I assumed they did something simple like the
keywords and and or, which respectively are just max and min. But, after
playing around with m & n for different values of m,n, I realized I had no idea
what was going on. It took an hour for me to see it had an intimate
relationship with powers of 2, and another hour to write a function (f_pos)
that was equivalent to it for positive integers. It took many more hours to
extend it to negative numbers, as well as unravel | and ^, which would've been
even harder without my initial work with &.

This process was thrilling as I "discovered" one after another property of the
operators. But it was also strange knowing that, as my solution got more and
more complicated, it become more and more peculiar that these were built-in
binary operators in Python unlike any I'd seen. I still don't know what these
functions are actually "doing" and what programming purpose they serve, but I
think at this point I've earned the right to actually read about them.

The following are the re-implementations of these operators, not including the
hundreds of Jupyter Notebook cells and scratchwork.
"""


def least_power(m):
    """
    Given a number m, return the greatest power of 2 <= m.
    Note this is the same as 2**int(math.log2(m)).
    """
    p = 1
    while p <= m:
        p *= 2
    p //= 2
    return p


def f_pos(m, n):
    """Re-implementation of the operator m & n for integers m,n > 0."""
    p = least_power(m)
    if m == p:
        return m*(n // m % 2)
    return f_pos(p, n) + f_pos(m - p, n)

def f(m, n):
    """Re-implementation of the operator m & n for any integers m,n."""
    if m == 0 or n == 0:
        return 0
    if m < n:
        m,n = n,m
    if n > 0:
        return f_pos(m,n)
    if m > 0:
        return f(m, n + 2*least_power(m))
    return m - f(m, -1 - n)

# for i in range(-1000,1000):
#     for j in range(-1000,1000):
#         if f(i, j) != (i & j):
#             print(i,j)

def g_pos(m, n):
    """Re-implementation of the operator m | n for integers m,n > 0."""
    p = least_power(m)
    if m == p:
        return m + n - m*(n//m % 2)
    return p * (1 - ((n // p) % 2)) + g(m - p, n)

def g(m, n):
    """Re-implementation of the operator m | n for any integers m,n."""
    if m == 0:
        return n
    if m < n:
        m,n = n,m
    if n < 0:
        return m - 1 - g(m, -n - 1)
    return g_pos(m, n)

# for i in range(-1000,1000):
#     for j in range(-1000,1000):
#         if g(i, j) != (i | j):
#             print(i,j)

def h(m, n):
    """Re-implementation of the operator m ^ n for integers m,n."""
    return g(m, n) - f(m, n)

# for i in range(-1000,1000):
#     for j in range(-1000,1000):
#         if (i ^ j) != h(i, j):
#             print(i,j)
