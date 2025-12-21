def busquedaBinaria(lista, buscado, inferior, superior):
    if inferior > superior:
        return -1, inferior, len(lista[inferior:])
    else:
        mitad = (superior + inferior) // 2

    if lista[mitad][0] == buscado:
        return mitad, len(lista[:mitad]), len(lista[mitad:])
    if buscado < lista[0][0]:
        return -1, 0, superior
    if buscado > lista[len(lista) - 1][0]:
        return -1, superior, inferior
    elif buscado < lista[mitad][0]:
        return busquedaBinaria(lista, buscado, inferior, mitad-1)
    else:
        return busquedaBinaria(lista, buscado, mitad+1, superior)

# --- INPUTS ---
numMarket = int(input().strip())
markets = []
for i in range(numMarket):
    id, numProd = map(int, input().strip().split())
    markets.append((numProd, id))

numQeries = int(input().strip())
queries = []
for i in range(numQeries):
    numProd = int(input().strip())
    queries.append(numProd)

markets.sort()

for numProd in queries:
    pos, sup, inf = busquedaBinaria(markets, numProd, 0, len(markets))
    if pos != -1:
        print(f"{markets[pos][1]} {sup} {inf}")
    else:
        print(f"NO {sup} {inf}")
