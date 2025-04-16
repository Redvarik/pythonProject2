n = int(input())
arr = list(map(int, input().split()))


new_arr = []
new_arr_index = n - 1

for i in range(n - 1, -1, -1):
    new_arr[new_arr_index] = arr[i]

    new_arr_index -= 1


print(' '.join(map(str, new_arr)))