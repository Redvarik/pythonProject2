s = input().strip()
result = 0
current_number = 0
operator = '+'

#
for char in s:
    if char.isdigit():
        current_number = current_number * 10 + int(char)
    else:
        if operator == '+':
            result += current_number
        elif operator == '-':
            result -= current_number
        operator = char
        current_number = 0

if operator == '+':
    result += current_number
elif operator == '-':
    result -= current_number

print(result)
