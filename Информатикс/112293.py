n = int(input())
a = list(map(int, input().split()))
min = -1
max = -1
for x in a:
    if x % 2 == 0 and x > 0:
        if min == -1 or x < min:
            min = x
        if max == -1 or x > max:
            max = x
print(min, max)
