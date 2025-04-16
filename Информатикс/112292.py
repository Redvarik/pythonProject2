n = int(input())
a = list(map(int, input().split()))

min_a = min(a)
for i in range(n):
    if a[i] == min_a:
        print(i + 1, end=' ')
