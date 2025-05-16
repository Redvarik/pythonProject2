import random
c = set()

for n in range(1, 100):
    n2 = bin(n)[2:]
    if n2.count("1") % 2 == 0:
        n2 += "00"
    else:
        n2 += "10"
    r = int(n2, 2)
    if r > 97:
        c.add(r)
print(min(c))
