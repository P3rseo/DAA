import heapq

def dijkstra(origen, grafo):
    n = len(grafo)
    distancias = [float('inf')] * n
    distancias[origen] = 0
    precedencias = [float('inf')] * n
    precedencias[origen] = origen
    visitados = [False] * n
    colaPrioridad = [(0,origen)]
    while colaPrioridad:
        distanciaMin, nodo = heapq.heappop(colaPrioridad)
        if visitados[nodo]:
            continue
        visitados[nodo] = True
        for (vecino, peso) in grafo[nodo]:
            if distanciaMin + peso < distancias[vecino]:
                distancias[vecino] = distanciaMin + peso
                precedencias[vecino] = nodo
                heapq.heappush(colaPrioridad, (distancias[vecino], vecino))
    return distancias, precedencias

entrada = input("").split(" ")
n = int(entrada[0])
m = int(entrada[1])
grafo = []
edsger = 0
for i in range(n+1):
    grafo.append([])
for i in range(m):
    entrada = input("").split(" ")
    u = int(entrada[0])
    v = int(entrada[1])
    w = int(entrada[2])
    grafo[u].append((v, w))
    grafo[v].append((u, w))
entrada = input("").split(" ")
c = int(entrada[0])
d = int(entrada[1])
for i in range(c):
    enemigoDisparado = int(input(""))
    distancias, precedencias = dijkstra(1, grafo)
    flag = False
    camino = []
    while True and not flag:
        if enemigoDisparado != 1:
            camino.append(enemigoDisparado)
            enemigoDisparado = precedencias[enemigoDisparado]
        else:
            flag = True
    print(*camino)