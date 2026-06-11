import heapq
def reconstruir_camino(origen, destino, precedencias):
    if precedencias[destino] == -1:
        return []

    camino = []
    actual = destino

    while actual != origen:
        camino.append(actual)
        actual = precedencias[actual]

    camino.append(origen)
    camino.reverse()

    return camino


def dijkstra(origen, g):
    # Inicializacion
    n = len(g)
    distancias = [float('inf')] * n
    distancias[origen] = 0

    precedencias = [-1] * n
    precedencias[origen] = origen

    visitados = [False] * n
    colaPrioridad = [(0, origen)]

    while colaPrioridad:
        distanciaMin, nodo = heapq.heappop(colaPrioridad)

        if visitados[nodo]:
            continue
        visitados[nodo] = True

        for vecino, peso in g[nodo]:
            if distanciaMin + peso < distancias[vecino]:
                distancias[vecino] = distanciaMin + peso
                precedencias[vecino] = nodo
                heapq.heappush(colaPrioridad, (distancias[vecino], vecino))
    return distancias, precedencias


numDispositivosRegistrados, numConexionesP2P = map(int, input().strip().split())

conexiones = [[] for _ in range(numDispositivosRegistrados)]
for _ in range(numConexionesP2P):
    d1, d2, nivelRiesgo = map(int, input().strip().split())
    conexiones[d1].append((d2, nivelRiesgo))
    conexiones[d2].append((d1, nivelRiesgo))

numVinculos = int(input().strip())

vinculos = []
for _ in range(numVinculos):
    id1, id2 = map(int, input().strip().split())
    vinculos.append([id1, id2])

for id1, id2 in vinculos:
    distancias, precedencias = dijkstra(id1, conexiones)
    print(f"{distancias[id2]}")
    camino = reconstruir_camino(id1, id2, precedencias)
    print(*camino)











