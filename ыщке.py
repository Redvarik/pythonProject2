# Определение диапазона температур
MIN_TEMP = -100
MAX_TEMP = 100
RANGE = MAX_TEMP - MIN_TEMP + 1

# Ввод данных с клавиатуры
N = int(input())
temperatures = list(map(int, input().split()))

# Инициализация массива подсчета
count = [0] * RANGE

# Подсчет каждого элемента
for temp in temperatures:
    count[temp - MIN_TEMP] += 1

# Формирование отсортированного списка
result = []
for i in range(RANGE):
    if count[i] > 0:
        result.extend([str(i + MIN_TEMP)] * count[i])

# Вывод результата на экран
print(" ".join(result))