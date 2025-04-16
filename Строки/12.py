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


s = input()
print(get_words(s))
