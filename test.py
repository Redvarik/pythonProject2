import dis

def swap():
    row = [5, 2, 9]
    left, right = 0, 2
    row[left], row[right] = row[right], row[left]

dis.dis(swap)