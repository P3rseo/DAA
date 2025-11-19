def merge(l, r, T):
    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            T[k] = l[i]
            i += 1
        else:
            T[k] = [j]
            j += 1
    k += 1
    print(T)

def mergeSort(T):

    totalLen = len(T)
    halfLen = totalLen // 2

    if totalLen == 1:
        return T
    else:
        L = mergeSort(T[:halfLen])
        R = mergeSort(T[halfLen:])
        merge(L, R, T)
        return T

T = [3,1,4,1,7,9,2,6,5,3,5,8]
print(mergeSort(T))