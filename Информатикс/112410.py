words = []

while True:
    line = input().strip()
    if not line:
        break
    word = line.split('. ', 1)[1]
    words.append(word)

words.sort()

for i, word in enumerate(words, start=1):
    print(f"{i}. {word}")
