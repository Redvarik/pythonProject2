def get_initials(full_name):
    parts = full_name.split()
    if len(parts) == 3:
        surname = parts[0]
        initials = parts[1][0] + "." + parts[2][0] + "."
        return f"{surname} {initials}"
    else:
        return "чот не то"


full_name = input()
print(get_initials(full_name))
