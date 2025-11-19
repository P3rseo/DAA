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
numCervezas, numConexiones = map(int, input().strip().split())
g = [[] for _ in range(numCervezas)]

for i in range(numConexiones):
    origen, vecino, peso = map(int, input().strip().split())
    g[origen].append((vecino, peso))
    g[vecino].append((origen, peso))

cervezaInicio, cervezaFinal = map(int, input().strip().split())

distancias, precedencias = dijkstra(cervezaInicio, g)
print(distancias[cervezaFinal])
camino = []
actual = cervezaFinal
flag = False
while True and not flag:
    camino.append(actual)
    if actual == cervezaInicio:
        flag = True
    else:
        actual = precedencias[actual]
camino.reverse()
print(*camino, sep=" ")
