import math as m


def f(x: float) -> float:
    return x * x * x + (60 * x) * x * x + 114 * x + 152


def hord():
    a, b = map(float, input().split())
    eps = 0.000004
    k = a
    i = 0
    while abs(f(k)) < eps and i < 1e12:
        k = (f(b) * a - f(a) * b) / (f(b) - f(a))
        if f(a) * f(k) < 0:
            b = k
        else:
            a = k
        i += 1
    return k


x = hord()
print(x)
print(f(x))
