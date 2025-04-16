import devs


def get_words_sorted_by_length(s):
    words = devs.get_words(s)
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(words[j]) > len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
    return words


s = input()
print(get_words_sorted_by_length(s))
