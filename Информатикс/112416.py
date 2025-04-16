expr = input().replace(" ", "")

i = 0
numbers = []
operators = []


def calculate(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b


current_num = 0
while i < len(expr):
    if expr[i].isdigit():
        current_num = current_num * 10 + int(expr[i])
    else:
        if operators and operators[-1] in '*/':
            op = operators.pop()
            prev_num = numbers.pop()
            current_num = calculate(prev_num, current_num, op)
        numbers.append(current_num)
        operators.append(expr[i])
        current_num = 0
    i += 1

if operators and operators[-1] in '*/':
    op = operators.pop()
    prev_num = numbers.pop()
    current_num = calculate(prev_num, current_num, op)
numbers.append(current_num)

result = numbers[0]
for i in range(1, len(numbers)):
    result = calculate(result, numbers[i], operators[i - 1])

print(result)
