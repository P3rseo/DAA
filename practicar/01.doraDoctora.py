import heapq

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


def dijkstra(origen, g, se_puede_pasar):
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

        for vecino, tiempo in g[nodo]:
            if not se_puede_pasar[vecino]:
                continue


            if dist + tiempo < distancias[vecino]:
                distancias[vecino] = dist + tiempo
                precedencias[vecino] = nodo
                heapq.heappush(colaPrioridad, (distancias[vecino], vecino))

    return distancias, precedencias



numLocalizaciones, numCalles, tiempoEnfermo = map(int, input().strip().split())

origen = -1
destino = -1
se_puede_pasar = [True] * numLocalizaciones

for _ in range(numLocalizaciones):
    partes = input().strip().split()
    idLocalizacion = int(partes[0])
    tipo = partes[1]

    if tipo == "enfermo":
        origen = idLocalizacion
    elif tipo == "hospital":
        destino = idLocalizacion

    if tipo == "plaza":
        se_puede_pasar[idLocalizacion] = False

calles = [[] for _ in range(numLocalizaciones)]

for _ in range(numCalles):
    c1, c2, tiempoRecorrerCalle, valorTrafico = map(int, input().strip().split())

    if valorTrafico < 5:    
        calles[c1].append((c2, tiempoRecorrerCalle))
        calles[c2].append((c1, tiempoRecorrerCalle))

distancias, precedencias = dijkstra(origen, calles, se_puede_pasar)

camino = reconstruir_camino(origen, destino, precedencias)

print(*camino)

if distancias[destino] < tiempoEnfermo:
    print("VE AL HOSPITAL")
else:
    print("ATIENDELE")