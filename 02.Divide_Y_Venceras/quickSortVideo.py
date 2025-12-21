def quicksort(lista, low, hi):
    if low >= hi:
        return 0

    start = low
    end = hi
    mid = (start + end) // 2
    pivot = lista[mid]

    while start <= end:
        while lista[start] < pivot:
            start += 1

        while lista[end] > pivot:
            end -= 1

        if start <= end:
            lista[start], lista[end] = lista[end], lista[start]
            start += 1
            end -= 1

    quicksort(lista, low, end)
    quicksort(lista, start, hi)


list = [5, 4, 3, 2, 1]
cambios = quicksort(list, 0, len(list) - 1)
print(*list)
