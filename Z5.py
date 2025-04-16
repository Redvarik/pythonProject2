def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def count_between_max_and_min(arr):
    sorted_arr = bubble_sort(arr)
    max_index = 0
    for i in range(1, len(arr)):
        if sorted_arr[i] > sorted_arr[max_index]:
            max_index = i

    min_index = len(arr) - 1
    for i in range(len(arr) - 2, -1, -1):
        if sorted_arr[i] < sorted_arr[min_index]:
            min_index = i

    return min_index - max_index - 1 if max_index < min_index else 0


array = list(map(int, input().split()))
result = count_between_max_and_min(array)
print(result)
