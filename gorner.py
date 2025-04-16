a = [0.0] * 1001
p, x = 0.0, 0.0
n = int(input("Введите степень многочлена n "))

print("Введите n+1 коэффициентов уравнения")
for i in range(n + 1):
    a[i] = float(input())

x = float(input("Введите X: "))
p = 0.0

for i in range(n + 1):
    p = p * x + a[i]

print("Значение многочлена = "f"{p:.6f}")
