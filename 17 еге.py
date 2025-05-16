a = 2461
r = set()

for i in range(2461, 9719 + 1):
    a += 1
    a0 = oct(a)
    if ((a//10) % 10) >= 3 and ((a//10) % 10) <= 7 and ((a // 100) % 10) != 1 and ((a // 100) % 10) != 9:
        r.add(a)
print(len(r))
print(max(r))
