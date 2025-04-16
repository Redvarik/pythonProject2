def extract_negatives(arr):
    negatives = [num for num in arr if num < 0]
    return negatives if negatives else [0]


N = int(input())
array = list(map(int, input().split()))
print(" ".join(map(str, extract_negatives(array))))
