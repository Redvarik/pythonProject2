a = 2476
r = []
for i in range(2476, 7857 + 1):
    a += 1
    if a % 2 == 0 and a % 8 != 0 and (a // 100) % 10 >= 7:
        r.append(a)
print(len(r))
print((min(r)+max(r))/2)
