def count_substring_occurrences(s, substring):
    count = 0
    len_s = len(s)
    len_sub = len(substring)
    for i in range(len_s - len_sub + 1):
        match = True
        # Проверяем, совпадает ли подстрока
        for j in range(len_sub):
            if s[i + j] != substring[j]:
                match = False
                break
        if match:
            count += 1

    return count


s = input()
substring = input()
print(count_substring_occurrences(s, substring))
