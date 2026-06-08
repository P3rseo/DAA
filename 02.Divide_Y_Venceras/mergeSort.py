def merge(v, left, right):
    l = 0
    r = 0
    i = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            v[i] = left[l]
            l += 1
        else:
            v[i] = right[r]
            r += 1
        i += 1

    # Copiar el resto (solo uno de los dos tendrá elementos pendientes)
    if l < len(left):
        resto = left
        f = l
    else:
        resto = right
        f = r

    for j in range(f, len(resto)):
        v[i] = resto[j]
        i += 1


def merge_sort(v):
    if len(v) == 1:
        return

    mid = len(v) // 2
    left = v[:mid]
    right = v[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(v, left, right)


#v = [3, 1, 4, 1, 7, 9, 2, 6, 5, 3, 5, 8]
v = [8, 3, 4, 12, 5, 6]
merge_sort(v)
print(v)
