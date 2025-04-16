def right_rotate(arr, n, r):
    r %= n
    for _ in range(r):
        last_element = arr.pop()
        arr.insert(0, last_element)
    return arr


n = int(input().strip())
arr = list(map(int, input().strip().split()))
r = int(input().strip())

print(" ".join(map(str, right_rotate(arr, n, r))))
