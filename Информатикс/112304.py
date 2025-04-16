def compress_array(arr, n):
    non_zero_elements = []
    zero_count = 0

    for num in arr:
        if num != 0:
            non_zero_elements.append(num)
        else:
            zero_count += 1
    arr = non_zero_elements + [0] * zero_count
    return arr


n = int(input().strip())
arr = list(map(int, input().strip().split()))
print(" ".join(map(str, compress_array(arr, n))))
