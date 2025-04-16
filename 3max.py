# main.py
from typing import List

# Функция для обработки массива

def process_array(arr: List[int]) -> List[int]:
    """
    Разделяет массив на нечетные числа (в порядке убывания индексов)
    и четные числа (в порядке возрастания индексов).

    :param arr: Входной массив чисел.
    :return: Новый массив с числами в нужном порядке.
    """
    odd_numbers = []  # Список для нечетных чисел
    even_numbers = []  # Список для четных чисел

    # Обход массива в обратном порядке для нечетных чисел
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 != 0:  # Проверка на нечетность
            odd_numbers.append(arr[i])

    # Обход массива в прямом порядке для четных чисел
    for i in range(len(arr)):
        if arr[i] % 2 == 0:  # Проверка на четность
            even_numbers.append(arr[i])

    # Объединяем два списка в результат
    return odd_numbers + even_numbers

# Основная часть программы
if __name__ == "__main__":
    # Пример входных данных
    input_array = [7, 2, 9, 4, 3, 6, 5, 8]

    # Обработка массива
    result = process_array(input_array)

    # Вывод результата
    print("Результат:", result)

