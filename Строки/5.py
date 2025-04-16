def extract_number(s):
    num_str = ''.join(filter(str.isdigit, s))
    print(num_str)
    if num_str:
        return int(num_str)**2
    else:
        return None


s = input()
print(extract_number(s))
