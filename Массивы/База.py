import random


i, j = 10, 10

matrix = [[random.randint(1, 100) for _ in range(j)] for _ in range(i)]

for row in matrix:
    print(row)
    