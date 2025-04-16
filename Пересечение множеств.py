# Ввод данных с клавиатуры
N, M = map(int, input().split())

# Ввод чисел первого и второго наборов
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Пересечение множеств и сортировка результата
result = sorted(set1 & set2)

# Вывод результата на экран
if result:
    print(" ".join(map(str, result)))
else:
    print()
