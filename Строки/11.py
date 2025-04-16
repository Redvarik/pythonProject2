
def count_words(s):
    word_count = 0
    in_word = False
    for char in s:
        if char != " ":
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False

    return word_count


s = input()
print(count_words(s))

