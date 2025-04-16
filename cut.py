def f(x: float) -> float:
    return x ** 3 + 60 *x **2 + 114 *x +152


a = -1000
b = 1000
h = 0.13
x = a

while x <= b:
    if f(x) * f(x + h) < 0 and -1 < f(x) < 1:
        print(f"{x:.2f} {x + h:.2f}")
    x += h
print(f(x))