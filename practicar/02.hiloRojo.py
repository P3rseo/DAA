def binary_search(lista, buscado, inferior, superior):
    if inferior > superior:
        return -1
    
    mitad = (inferior + superior) // 2

    if lista[mitad] == buscado:
        return mitad
    elif lista[mitad] > buscado:
        return binary_search(lista, buscado, inferior, mitad-1)
    else:
        return binary_search(lista, buscado, mitad+1, superior)



personasG1 = int(input().strip())
idsGrupo1 = list(map(int, input().strip().split()))
personasG2 = int(input().strip())
idsGrupo2 = list(map(int, input().strip().split()))
numParejasConectadas = int(input().strip())
conexiones = []
for _ in range(numParejasConectadas):
    id1, id2 = map(int, input().strip().split())
    conexiones.append([id1, id2])




for id1, id2 in conexiones:
    pos1 = binary_search(idsGrupo1, id1, 0, len(idsGrupo1) - 1)
    pos2 = binary_search(idsGrupo2, id2, 0, len(idsGrupo2) - 1)
    
    if pos1 == -1 or pos2 == -1:
        print("SIN DESTINO")
    else:
        print(f"{pos1} {pos2}")
        