def select_every_third(N, arr):
    result = [arr[i] for i in range(0, N, 3)]
    return result


N = int(input())
array = list(map(int, input().split()))
print(" ".join(map(str, select_every_third(N, array))))