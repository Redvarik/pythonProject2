n = int(input())
mass = map(int, input().split())
mass = list(mass)
x = int(input())
count = 0
for i in mass:
    if x == i:
        count = count + 1
print(count)