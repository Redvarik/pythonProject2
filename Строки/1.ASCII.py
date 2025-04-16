def print_ascii_table():
    for i in range(0, 10000):
        if i % 16 == 0 and i != 0:
            print()
        print(f"{i:3}:{chr(i)}", end=" ")
    print()
#123