def right_rotate_subarray(arr, n, k, m, r):
    k -= 1
    m -= 1
    sub_len = m - k + 1
    r %= sub_len

    for _ in range(r):
        last_element = arr[m]
        for i in range(m, k, -1):
            arr[i] = arr[i - 1]
        arr[k] = last_element
    return arr


n = int(input().strip())
arr = list(map(int, input().strip().split()))
k, m = map(int, input().strip().split())
r = int(input().strip())
print(" ".join(map(str, right_rotate_subarray(arr, n, k, m, r))))
