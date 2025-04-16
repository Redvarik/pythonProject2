n = int(input())
arr = list(map(int, input().split()))

new_arr = []

for i in range(n-1, -1, -1):
    new_arr.append(arr[i])


print(' '.join(map(str, new_arr)))
