employees = []

while True:
    line = input().strip()
    if not line:
        break
    parts = line.rsplit(' ', 1)
    if len(parts) == 2:
        initials, surname = parts
        employees.append((surname, initials))

employees.sort()

for i, (surname, initials) in enumerate(employees, start=1):
    print(f"{i}. {initials} {surname}")
