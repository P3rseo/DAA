def binarySearch(T, x, L, H):
    if L > H:
        return False
    else:
        k = (L + H) // 2
        if T[k] == x:
            return k
        elif T[k] < x:
            return binarySearch(T, x, k + 1, H)
        else:
            return binarySearch(T, x, L, k - 1)


x = 7
T = [-2, 0, 3, 7, 7, 9, 10, 12, 23, 24, 30]
L = 0
H = len(T) - 1

print(binarySearch(T, x, L, H))