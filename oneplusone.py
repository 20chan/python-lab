# original code
# print(1+1)

import math


def c(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

n, m = 100000, 100
a = 4 * sum([((-1)**k)/(2*k+1) for k in range(n)]) / math.pi
b = sum(1/math.factorial(k) for k in range(m)) / math.e

print(a + b)
