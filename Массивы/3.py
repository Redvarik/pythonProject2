import random
import devs

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
M = int(input("M="))
matrix = devs.matrix_create(N, M)

print("Исходная матрица:")
for row in matrix:
    print(row)


flip_vertical(matrix)

print("\nПосле отражения:")
for row in matrix:
    print(row)