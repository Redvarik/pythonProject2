
n = int(input())

print()
days = list(map(int, input().split()))



# Разделяем дни на четные и нечетные
odd_days = [day for day in days if day % 2 != 0]  # Нечетные дни
even_days = [day for day in days if day % 2 == 0]  # Четные дни

# Определяем результат
result = "YES" if len(even_days) >= len(odd_days) else "NO"

# Вывод результатов
print(" ".join(map(str, odd_days)))
print(" ".join(map(str, even_days)))
print(result)
