def remove_duplicate_chars(s):
    result = ""
    i = 0
    n = len(s)

    while i < n:
        if i + 1 < n and s[i] == s[i + 1]:
            current_char = s[i]
            while i < n and s[i] == current_char:
                i += 1
        else:
            result += s[i]
            i += 1

    return result


s = input()
print(remove_duplicate_chars(s))