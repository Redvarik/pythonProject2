def find_longest_sequence(arr):
    max_len = 1  # Длина текущей цепочки
    result_len = 1  # Максимальная длина цепочки
    result_element = arr[0]  # Элемент, который встречается максимальное число раз подряд

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            max_len += 1
        else:
            if max_len > result_len:
                result_len = max_len
                result_element = arr[i - 1]
            max_len = 1

    # Проверяем последнюю цепочку
    if max_len > result_len:
        result_len = max_len
        result_element = arr[-1]

    return result_element, result_len


# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Поиск самой длинной цепочки
element, length = find_longest_sequence(arr)

# Вывод результата
print(element, length)
