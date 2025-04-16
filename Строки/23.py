import devs
def count_unique_letters(word):
    unique_letters = set()
    for char in word:
        if char.isalpha():
            unique_letters.add(char.lower())
    return len(unique_letters)


word = input()
print(count_unique_letters(word))
