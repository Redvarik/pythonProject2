def is_number(word):
    try:
        float(word)
        return True
    except ValueError:
        return False


word = input()
if is_number(word):
    print("число")
else:
    print("не число")
