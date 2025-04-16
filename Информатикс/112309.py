N = int(input())
elements = list(map(int, input().split()))
count_dict = {}

for element in elements:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1

result = []

for element in elements:
    if count_dict[element] > 1:
        result.append(element)
        count_dict[element] = 0

if len(result) == 0:
    print(0)
else:
    print(" ".join(map(str, result)))