def separate_array(N, arr):
    positive = []
    zero = []
    negative = []

    for num in arr:
        if num > 0:
            positive.append(num)
        elif num == 0:
            zero.append(num)
        else:
            negative.append(num)

    result = positive + zero + negative
    return result


N = int(input())
array = list(map(int, input().split()))
print(" ".join(map(str, separate_array(N, array))))
