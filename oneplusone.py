# original code
# print(1+1)

import functools
from math import pi, e


def factorial(n):
    return 1 if n == 0 else functools.reduce(lambda i, j: i*j, range(1, n+1))


def c(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)


def sigma(f, n, r):
    return sum(f(k) for k in range(n, r))

a = 4 * sigma(lambda k: ((-1)**k)/(2*k+1), 0, 100000) / pi
b = sigma(lambda k: 1/factorial(k), 0, 1000) / e

print(a + b)
