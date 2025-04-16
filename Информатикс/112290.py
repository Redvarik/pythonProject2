N = int(input())  # Размер массива
arr = list(map(int, input().split()))  # Массив чисел
X = int(input())  # Заданное число

# Список для хранения индексов элементов, равных X
indices = []

# Проходим по массиву и ищем элементы, равные X
for i in range(N):
    if arr[i] == X:
        indices.append(i + 1)  # Индексы начинаются с 1, а не с 0

# Если такие элементы найдены, выводим их индексы, иначе -1
if indices:
    print(*indices)
else:
    print(-1)
