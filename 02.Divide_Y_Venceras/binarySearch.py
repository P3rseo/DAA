def busquedaBinaria(lista, buscado, inferior, superior):
    if inferior > superior:
        return -1
    else:
        mitad = (superior + inferior) // 2

    if lista[mitad] == buscado:
        return mitad
    elif buscado < lista[mitad]:
        return busquedaBinaria(lista, buscado, inferior, mitad-1)
    else:
        return busquedaBinaria(lista, buscado, mitad+1, superior)


T = [-3, -1, 0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 16, 17]
inf = 0
sup = len(T)
buscado = 12
pos = busquedaBinaria(T, buscado, inf, sup)
print(pos)
