def count_letters(word):
    letter_count = [0] * 26
    for char in word.lower():
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            letter_count[index] += 1
    return letter_count


def are_anagrams(word1, word2):
    count1 = count_letters(word1)
    count2 = count_letters(word2)
    return count1 == count2


word1 = input()
word2 = input()
if are_anagrams(word1, word2):
    print("анаграмма")
else:
    print("нет")
