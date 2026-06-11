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


numDispositivosRegistrados, numConexionesP2P = map(int, input().strip().split())

conexiones = [[] for _ in range(numDispositivosRegistrados)]

for _ in range(numConexionesP2P):
    id1, id2, nivelRiesgo = map(int, input().strip().split())
    conexiones[id1].append((id2, nivelRiesgo))
    conexiones[id2].append((id1, nivelRiesgo))

numVinculos = int(input().strip())

vinculos = []

for _ in range(numVinculos):
    id1, id2 = map(int, input().strip().split())
    vinculos.append((id1, id2))

for id1, id2 in vinculos:
    distancias, precedencias = dijkstra(id1, conexiones)
    print(distancias[id2])
    camino = reconstruir_camino(id1, id2, precedencias)
    print(*camino)




"""
print(numDispositivosRegistrados)
print(numConexionesP2P)

for conexion in conexiones:
    print(conexion)

print(numVinculos)

for vinculo in vinculos:
    print(vinculo)
"""