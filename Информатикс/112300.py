a = int(input())
n = list(map(int, input().split()))
r = int(input())

for k in range(r):
    y = n[0]
    n.pop(0)
    for i in range(1):
        n.append(y)

print(*n)
