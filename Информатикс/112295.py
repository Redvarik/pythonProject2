n = int(input())
arr = list(map(int, input().split()))


for i in range(1, n, 2):
    arr[i-1], arr[i] = arr[i], arr[i-1]


print(' '.join(map(str, arr)))
