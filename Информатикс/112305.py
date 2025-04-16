def compress_array(N, arr):
    seen = set()
    for i in range(N):
        if arr[i] in seen:
            arr[i] = 0
        else:
            seen.add(arr[i])

    non_zero_index = 0
    for i in range(N):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    for i in range(non_zero_index, N):
        arr[i] = 0

    return arr


N = int(input())
array = list(map(int, input().split()))
print(" ".join(map(str, compress_array(N, array))))
