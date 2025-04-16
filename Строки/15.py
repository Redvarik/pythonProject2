import devs


def count_letters_in_words(s):
    words = devs.get_words(s)
    letter_counts = []

    for word in words:
        count = 0
        for char in word:
            if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                count += 1
        letter_counts.append(count)

    return letter_counts


s = input()
print(count_letters_in_words(s))
