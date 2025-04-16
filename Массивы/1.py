import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


N, M = 3, 6
matrix = [[random.randint(1, 9) for _ in range(M)] for _ in range(N)]
print("Исходная матрица:")
for row in matrix:
    print(row)

sorted_rows = [bubble_sort(row.copy()) for row in matrix]
print("\nСтроки отсортированы:")
for row in sorted_rows:
    print(row)
