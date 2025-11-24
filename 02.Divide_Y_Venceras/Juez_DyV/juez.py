def binary_search(datos, buscado, inf, sup):
    if inf > sup:
        return -1
    else:
        mitad = (sup + inf) // 2

        if datos[mitad] == buscado:
            return mitad
        elif buscado < datos[mitad]:
            return binary_search(datos, buscado, inf, mitad-1)
        else:
            return binary_search(datos, buscado, mitad+1, sup)

datos = [1,3,5,6,7,9]
buscado = 5
inf = 0
sup = len(datos)
pos = binary_search(datos, buscado, inf, sup)
print(pos)