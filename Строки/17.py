def sort_string_ascii(s):
    chars = list(s)
    n = len(chars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ord(chars[j]) > ord(chars[j + 1]):
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
    return "".join(chars)


s = input()
print(sort_string_ascii(s))
