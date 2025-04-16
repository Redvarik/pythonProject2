def sum_of_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total


s = input()
print(sum_of_digits(s))
