
def busquedaBinaria(lista, buscado, inferior, superior):
    if inferior > superior:
        print("El numero no esta en la lista")
        return -1
    else:
        mitad = (superior + inferior) // 2
        print(f"La mitad es {mitad}")

    if lista[mitad] == buscado:
        print(f"Se ha encontrado el numero {buscado} en la posicion {mitad}")
        return mitad
    elif buscado < lista[mitad]:
        print(f"El numero {buscado} es mas pequeño que {lista[mitad]}")
        return busquedaBinaria(lista, buscado, inferior, mitad-1)
    else:
        print(f"El numero {buscado} es mas grande que {lista[mitad]}")
        return busquedaBinaria(lista, buscado, mitad+1, superior)


T = [-3, -1, 0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 16, 17]
inf = 0
sup = len(T)
buscados = [6, -1]
for buscado in buscados:
    pos = busquedaBinaria(T, buscado, inf, sup)
    print(pos)
    print("\n\n\n")
