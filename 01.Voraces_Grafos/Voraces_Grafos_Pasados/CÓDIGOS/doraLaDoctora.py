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
t = int(entrada[2])
grafo = []
noValidos = []
enfermo = 0
hospital = 0
for i in range(n):
    grafo.append([])
    entrada = input("").split(" ")
    e = int(entrada[0])
    d = entrada[1]
    if d == "plaza":
        noValidos.append(e)
    if d == "enfermo":
        enfermo = e
    if d == "hospital":
        hospital = e
for i in range(m):
    entrada = input("").split(" ")
    o = int(entrada[0])
    d = int(entrada[1])
    w = int(entrada[2])
    c = int(entrada[3])
    if not(o in noValidos or d in noValidos or c >= 5):
        grafo[o].append((d, w))
        grafo[d].append((o, w))
distancias, precedencias = dijkstra(enfermo, grafo)
camino = []
actual = hospital
flag = 0
while True and not flag:
    camino.append(actual)
    if actual == enfermo:
        flag = 1
    else:
        actual = precedencias[actual]
camino.reverse()
print(*camino)
if (distancias[hospital] < t):
    print("VE AL HOSPITAL")
else:
    print("ATIENDELE")