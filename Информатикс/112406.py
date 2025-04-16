s = input()
n = 0
id = s.find('R')
rez = ''
sh = 0

for i in range(id, len(s)):
    if s[i] != 'B':
        rez = rez + s[i]
    else:
        sh += 1

print(s[:id] + rez)
print(sh)
