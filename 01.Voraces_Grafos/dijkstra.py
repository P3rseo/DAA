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