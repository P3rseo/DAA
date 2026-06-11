import heapq

def dijkstra(origen, g):
    # Inicializacion
    n = len(g)
    distancias = [float('inf')] * n
    distancias[origen] = 0

    precedencias = [float('inf')] * n
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


# Grafo como lista de adyacencia: g[u] = [(v, peso), ...]
g = [
    [(1, 2), (2, 5)],  # 0 -> 1 (2), 0 -> 2 (5)
    [(2, 1), (3, 2)],  # 1 -> 2 (1), 1 -> 3 (2)
    [(3, 1), (4, 5)],  # 2 -> 3 (1), 2 -> 4 (5)
    [(4, 3)],          # 3 -> 4 (3)
    []                 # 4 (sin salidas)
]

origen = 0
distancias, precedencias = dijkstra(origen, g)
print("distancias:", distancias)
print("precedencias:", precedencias)





import heapq


def dijkstra(origen, g):

    n = len(g)
    distancias = [float("inf")] * n
    distancias[origen] = 0

    padres = [-1] * n
    padres[origen] = origen

    colaPrioridad = [(0, origen)]

    while colaPrioridad:
        distMin, nodo = heapq.heappop(colaPrioridad)

        if distMin != distancias[nodo]:
            continue

        for vecino, peso in g[nodo]:
            if distMin + peso < distancias[vecino]:
                distancias[vecino] = distMin + peso
                padres[vecino] = nodo
                heapq.heappush(colaPrioridad, (distancias[vecino], vecino))

    return distancias, padres


def reconstruir_camino(origen, destino, padres):
    if padres[destino] == -1:
        return []

    camino = []
    actual = destino

    while actual != origen:
        camino.append(actual)
        actual = padres[actual]

    camino.append(origen)
    camino.reverse()

    return camino