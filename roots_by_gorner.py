from math import gcd


def divisors(n):  # поиск делителей
    result = set()
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.add(i)
            result.add(-i)
    return result


def rational_roots(coef):
    # Старший и свободный коэф
    a_n = coef[0]
    a_0 = coef[-1]
    a_n = abs(a_n)
    # Делит старшего и свободного коэф
    divisors_a_n = divisors(a_n)
    divisors_a_0 = divisors(a_0)

    # Возможные рациональные корни
    possible_roots = set()
    for p in divisors_a_0:
        for q in divisors_a_n:
            possible_roots.add(p / q)

    # Проверяем каждый возможный корень по схеме Горнера
    roots = []
    for root in possible_roots:
        result = coef[0]
        for i in range(1, len(coef)):
            result = result * root + coef[i]
        if result == 0:
            roots.append(root)

    return roots


coef = [1, -6, 7, 0, 18]
roots = rational_roots(coef)
print("Рациональные корни многочлена:", roots)
