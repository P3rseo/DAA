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



# --- INPUTS ---
roomNum, doorNum, maxTime = map(int, input().strip().split())

g = [[] for i in range(roomNum)]

for door in range(doorNum):
    r1, r2, d = map(int, input().strip().split())
    g[r1].append((r2, d))
    g[r2].append((r1, d))

distancias, precedencias = dijkstra(0, g)

tiempoTotal = sum(dist for dist in distancias)
if (tiempoTotal > maxTime):
    print("Aleg, ¡a decorar!")
else:
    print(tiempoTotal)
