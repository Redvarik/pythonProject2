s = input().strip()
last_b = s.rfind('B')
total_r = s.count('R')

if last_b == -1:
    print(s)
    print(0)
else:
    r_after = s[last_b+1:].count('R')
    removed = total_r - r_after
    res = []
    for c in s:
        if c == 'B':
            res.append(c)
    res.extend(list(s[last_b+1:]))
    print(''.join(res))
    print(removed)