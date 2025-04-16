n = int(input())
words = []

for _ in range(n):
    line = input().strip()
    word = line.split('. ', 1)[1]
    words.append(word)

words.sort()

for i, word in enumerate(words, start=1):
    print(f"{i}. {word}")
