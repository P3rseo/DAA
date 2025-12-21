def binarySearch(lista, buscado, inferior, superior):
    if inferior > superior or buscado < lista[0] or buscado > lista[len(lista) - 1]:
        return -1
    else:
        mitad = (superior + inferior) // 2

    if lista[mitad] == buscado:
        return mitad
    elif buscado < lista[mitad]:
        return binarySearch(lista, buscado, inferior, mitad-1)
    else:
        return binarySearch(lista, buscado, mitad+1, superior)


# --- INPUTS ---
# Numero de personas en el grupo 1 y sus respectivos identificadores
numPersonasG1 = int(input().strip())
grupo1 = list(map(int, input().strip().split()))

# Numero de personas en el grupo 2 y sus respectivos identificadores
numPersonasG2 = int(input().strip())
grupo2 = list(map(int, input().strip().split()))

# Numero de parejas conectadas y sus identificadores
parejasConectadas = int(input().strip())
conectadas = []
for _ in range(parejasConectadas):
    id1, id2 = map(int, input().strip().split())
    conectadas.append((id1, id2))

# --- OUTPUT ---
for pareja in conectadas:
    id1, id2 = pareja
    posG1 = binarySearch(grupo1, id1, 0, len(grupo1))
    posG2 = binarySearch(grupo2, id2, 0, len(grupo2))
    if posG1 == -1 or posG2 == -1:
        print(f"SIN DESTINO")
    else:
        print(f"{posG1} {posG2}")
