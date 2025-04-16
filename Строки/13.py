def get_sorted_words(s):
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

    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]
    return words


s = input()
print(get_sorted_words(s))
