def merge(v, left, right):
    l = 0
    r = 0
    i = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            v[i] = left[l]
            l += 1
        else:
            v[i] = right[r]
            r += 1
        i += 1
    
    if l < len(left):
        f = l
        resto = left
    else:
        f = r
        resto = right

    for j in range(f, len(resto)):
        v[i] = resto[j]
        i += 1


def merge_sort(v):
    if len(v) == 1:
        return v
    mid = len(v) // 2
    left = v[:mid]
    right = v[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(v, left, right)



V = [38, 27, 43, 3, 9, 82, 10, -5, 10, 0, -1, 15, 94, 23, 7, 12]
merge_sort(V)
print(V)