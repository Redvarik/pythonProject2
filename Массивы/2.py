import random


def flip_horizontal_in_place(matrix):
    n = len(matrix)
    for i in range(n // 2):  # Идём до середины
        j = n - 1 - i        # Индекс зеркальной строки
        matrix[i], matrix[j] = matrix[j], matrix[i]


N = 3
matrix = [[random.randint(1, 9) for _ in range(N)] for _ in range(N)]

print("Исходная матрица:")
for row in matrix:
    print(row)

flip_horizontal_in_place(matrix)

print("\nПосле отражения:")
for row in matrix:
    print(row)
