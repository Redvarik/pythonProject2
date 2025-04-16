def remove_extra_spaces(s):
    result = ""
    prev_char = " "

    for char in s:
        if char != " " or prev_char != " ":
            result += char
        prev_char = char

    return result.strip()


s = input()
print(remove_extra_spaces(s))
