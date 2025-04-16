def left_rotate_subarray(arr, n, k, m, r):
    k -= 1
    m -= 1
    sub_len = m - k + 1
    r %= sub_len

    for _ in range(r):
        first_element = arr[k]
        for i in range(k, m):
            arr[i] = arr[i + 1]
        arr[m] = first_element

    return arr


n = int(input().strip())
arr = list(map(int, input().strip().split()))
k, m = map(int, input().strip().split())
r = int(input().strip())

print(" ".join(map(str, left_rotate_subarray(arr, n, k, m, r))))
