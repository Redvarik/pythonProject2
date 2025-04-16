def remove_middle_chars(s):
    length = len(s)
    result = ""
    if length % 2 == 1:
        middle = length // 2
        for i in range(length):
            if i != middle:
                result += s[i]
    else:
        middle1 = length // 2 - 1
        middle2 = length // 2
        for i in range(length):
            if i != middle1 and i != middle2:
                result += s[i]
    return result


s = input()
print(remove_middle_chars(s))
