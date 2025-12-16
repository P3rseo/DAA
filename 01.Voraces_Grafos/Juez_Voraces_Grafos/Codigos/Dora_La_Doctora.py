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
numLocations, numStreets, maxTime = map(int, input().strip().split())

g = []
origen = 0
destino = 0
noValido = []
locations = []

for i in range(numLocations):
    g.append([])
    partes = input().strip().split()
    locationID = int(partes[0])
    locationType = partes[1]
    if locationType == 'enfermo':
        origen = locationID
    if locationType == 'hospital':
        destino = locationID
    if locationType == 'plaza':
        noValido.append(locationID)
    locations.append((locationID, locationType))

for i in range(numStreets):
    src, dst, time, density = map(int, input().strip().split())

    if not(src in noValido or dst in noValido or density >= 5):
        g[src].append((dst, time))
        g[dst].append((src, time))

distancias, precedencias = dijkstra(origen, g)

camino = []
actual = destino
flag = 0
while True and not flag:
    camino.append(actual)
    if actual == origen:
        flag = 1
    else:
        actual = precedencias[actual]
camino.reverse()
print(*camino)
if (distancias[destino] < maxTime):
    print("VE AL HOSPITAL")
else:
    print("ATIENDELE")