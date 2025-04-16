def rearrange_in_place(arr):
    n = len(arr)

    neg_idx = 0
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[neg_idx] = arr[neg_idx], arr[i]
            neg_idx += 1

    zero_idx = neg_idx
    for i in range(neg_idx, n):
        if arr[i] == 0:
            arr[i], arr[zero_idx] = arr[zero_idx], arr[i]
            zero_idx += 1

    return arr


array = list(map(int, input().split()))
result = rearrange_in_place(array)
print(result)
