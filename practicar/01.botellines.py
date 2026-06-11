import heapq

def reconstruir_caminos(origen, destino, precedencias):
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
    n = len(g)

    distancias = [float('inf')] * n
    distancias[origen] = 0

    precedencias = [-1] * n
    precedencias[origen] = origen

    visitados = [False] * n
    colaPrioridad = [(0, origen)]

    while colaPrioridad:
        dist, nodo = heapq.heappop(colaPrioridad)

        if visitados[nodo]:
            continue
        visitados[nodo] = True

        for vecino, peso in g[nodo]:
            if dist + peso < distancias[vecino]:
                distancias[vecino] = dist + peso
                precedencias[vecino] = nodo
                heapq.heappush(colaPrioridad, (distancias[vecino], vecino))

    return distancias, precedencias



numCervezas, numConexiones = map(int, input().strip().split())

conexiones = [[] for _ in range(numCervezas)]

for _ in range(numConexiones):
    c1, c2, dst = map(int, input().strip().split())
    conexiones[c1].append((c2, dst))
    conexiones[c2].append((c1, dst))

cInicio, cFin = map(int, input().strip().split())

distancias, precedencias = dijkstra(cInicio, conexiones)
print(distancias[cFin])
camino = reconstruir_caminos(cInicio, cFin, precedencias)
print(*camino)