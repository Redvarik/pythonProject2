s = input().strip()
n = len(s)

prefix_R = [0] * (n + 1)
for i in range(n):
    prefix_R[i + 1] = prefix_R[i] + (s[i] == 'R')

suffix_B = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix_B[i] = suffix_B[i + 1] + (s[i] == 'B')

min_total = float('inf')
best_split = -1

for split_pos in range(n + 1):
    k = prefix_R[split_pos]
    m = suffix_B[split_pos]
    if k == m and k + m < min_total:
        min_total = k + m
        best_split = split_pos

result_str = s[:best_split].replace('R', '') + s[best_split:].replace('B', '')
print(result_str)
print(min_total)