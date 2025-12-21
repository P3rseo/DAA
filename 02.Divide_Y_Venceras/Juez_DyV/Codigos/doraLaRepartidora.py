def busquedaBinaria(lista, buscado, inferior, superior, coindidencias):
    if inferior > superior:
        return -1, coincidencias[inferior][0], coindidencias[inferior][1]
    else:
        mitad = (superior + inferior) // 2

    if lista[mitad][0] == buscado:
        return mitad, coincidencias[mitad][0], coincidencias[mitad][1]
    if buscado < lista[0][0]:
        return -1, 0, superior
    if buscado > lista[len(lista) - 1][0]:
        return -1, superior, inferior
    elif buscado < lista[mitad][0]:
        return busquedaBinaria(lista, buscado, inferior, mitad-1, coincidencias)
    else:
        return busquedaBinaria(lista, buscado, mitad+1, superior, coincidencias)


# --- INPUTS ---
numMarket = int(input().strip())
markets = []
for i in range(numMarket):
    id, numProd = map(int, input().strip().split())
    markets.append((numProd, id))

markets.sort()

coincidencias = []
for i in range(len(markets)):
    menores = i
    mayorIgual = len(markets)-i
    coincidencias.append((menores, mayorIgual))

numQeries = int(input().strip())
queries = []
for i in range(numQeries):
    numProd = int(input().strip())
    queries.append(numProd)

for numProd in queries:
    pos, sup, inf = busquedaBinaria(markets, numProd, 0, len(markets), coincidencias)
    if pos != -1:
        print(f"{markets[pos][1]} {sup} {inf}")
    else:
        print(f"NO {sup} {inf}")

