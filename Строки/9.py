def remove_leading_spaces(s):
    result = ""
    i = 0
    length = len(s)
    while i < length and s[i] == " ":
        i += 1
    while i < length:
        result += s[i]
        i += 1
    return result


s = input()
print(remove_leading_spaces(s))
