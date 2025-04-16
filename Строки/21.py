def find_word_parts(word):
    vowels = "аеёиоуыэюяaeiouy"
    for i in range(1, len(word)):
        if word[i] in vowels:
            part1 = word[:i]
            part2 = word[i + 1:]
            if len(part1) == len(part2):
                return part1, part2
    return None


word = input()
parts = find_word_parts(word)
if parts:
    print(f"Части слова: {parts[0]} {parts[1]}")
else:
    print("Нема")
