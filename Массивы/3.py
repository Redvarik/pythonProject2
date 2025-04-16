import random


def flip_vertical(matrix):
    n = len(matrix)
    for row in matrix:
        left = 0
        right = n - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1


N = int(input("N="))
matrix = [[random.randint(1, 9) for _ in range(N)] for _ in range(N)]

print("Исходная матрица:")
for row in matrix:
    print(row)


flip_vertical(matrix)

print("\nПосле отражения:")
for row in matrix:
    print(row)