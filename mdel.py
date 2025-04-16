import math as m


def f(x):
    return x ** 3 + 4 * x ** 2 - 3 * x - 6


a = 1.26
b = 1.39
eps = 0.000001

while b - a > eps:
    x = (a + b) / 2
    if f(a) * f(x) < 0:
        b = x
    else:
        a = x

print(f"{a:.6f}  {f(x)}")
