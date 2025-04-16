import devs as d


def remove_letters(x, z):
    x = d.lower(x)
    x_list = list(x)
    i = 0
    while i < len(x_list):
        if x_list[i] in z:
            del x_list[i]
        else:
            i += 1
    return "".join(x_list)


x = input()
z = input()
print(remove_letters(x, z))
