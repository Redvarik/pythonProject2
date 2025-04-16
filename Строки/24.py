import devs as d


def count_letters(word):
    letter_count = [0] * 26
    for char in word.lower():
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')  # Индекс буквы в списке (0 для 'a', 1 для 'b')
            letter_count[index] += 1
    return letter_count


def can_form_word(a, b):
    count_a = count_letters(a)
    count_b = count_letters(b)

    for i in range(26):
        if count_b[i] > count_a[i]:
            return False
    return True


a = input("A: ")
b = input("B: ")
if can_form_word(a, b):
    print("Можно")
else:
    print("Нельзя")
