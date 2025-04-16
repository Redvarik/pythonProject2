def reverse_array_part(arr, k, m):
    if k < 1 or k > len(arr) or m < 1 or m > len(arr):
        raise IndexError()
    left = k - 1
    right = m - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


n = int(input())
arr = list(map(int, input().split()))
k, m = map(int, input().split())

reverse_array_part(arr, k, m)

print(' '.join(map(str, arr)))
