def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# Чтение входных данных
n, k = map(int, input().split())
first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

# Поиск элементов второго массива в первом
for num in second_array:
    if binary_search(first_array, num):
        print("YES")
    else:
        print("NO")
