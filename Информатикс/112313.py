def get_last_digit(num):
    return num % 10


def sort_by_last_digit(arr):
    # Сортировка с использованием ключа - последняя цифра числа
    return sorted(arr, key=get_last_digit)


# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Сортировка массива
sorted_arr = sort_by_last_digit(arr)

# Вывод результата
print(*sorted_arr)
