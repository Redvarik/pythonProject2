def sr_kvd(n):
    sr = sum(n) / 5
    s = 0
    for i in n:
        s += (i - sr) ** 2
    s = (s / 5) ** 0.5
    return s


def mile_to_km(e):
    return float(e) * 1, 609


def year_to_hour(s):
    return float(s) * 8760


def kzt_to_uah(v):
    return v * 0.209593 / 2.4


def is_password_good(ps):
    word_a = 'qwertyuiopasdfghjklzxcvbnm'
    word_A = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    numb = '1234567890'

    if len(ps) >= 8:
        for i in word_a:
            if i in ps:
                f1 = 1
                break
        for i in word_A:
            if i in ps:
                f2 = 1
                break
        for i in numb:
            if i in ps:
                f3 = 1
                break
    if f1 == f3 == f2 == 1:
        return True


def unique(obj: iter):
    args = []
    for i in obj:
        if i not in args:
            args.append(i)
            yield i


def bubble(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def get_words(s):
    words = []
    current_word = ""
    for char in s:
        if char != " ":
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)
    return words


def lower(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


def count_letters(word):
    letter_count = [0] * 26
    for char in word.lower():
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            letter_count[index] += 1
    return letter_count


def bubble_sort_letters(s):
    chars = list(s)
    n = len(chars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if chars[j] > chars[j + 1]:
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
    return ''.join(chars)
