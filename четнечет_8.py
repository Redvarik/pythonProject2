# Функция проверки условия
def is_valid(num):
    if num % 2 != 0:  # Число должно быть четным
        return False
    octal_str = oct(num)[2:]  # Преобразуем число в восьмеричную систему
    if len(octal_str) < 3:  # Если число короче 3 символов в восьмеричной системе
        return False
    return int(octal_str[-3]) % 2 == 1  # Проверяем, нечетна ли третья справа цифра

# Ввод данных с клавиатуры
n = int(input())
numbers = map(int, input().split())

# Отбор чисел, удовлетворяющих условию
result = sorted(filter(is_valid, numbers))

# Вывод результата
print(len(result))
if result:
    print(" ".join(map(str, result)))