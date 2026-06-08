def binsearch(lista, buscado, inferior, superior):
    if inferior > superior:
        return -1
    
    mitad = (superior + inferior) // 2
    if lista[mitad] == buscado:
        return mitad
    elif buscado < lista[mitad]:
        return binsearch(lista, buscado, inferior, mitad-1)
    else:
        return binsearch(lista, buscado, mitad+1, superior)
    

T = [-3, -1, 0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 16, 17]
inf = 0
sup = len(T) - 1
buscado = 8
pos = binsearch(T, buscado, inf, sup)
print(pos)