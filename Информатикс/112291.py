n = int(input())
a = list(map(int, input().split()))
mx = max(a)
cnt = 0
for x in a:
    if x == mx:
        cnt += 1
print(mx, cnt)
