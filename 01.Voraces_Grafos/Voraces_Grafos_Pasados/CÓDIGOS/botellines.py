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
grafo = [[] for _ in range(n)]

for i in range(m):
    entrada = input("").split(" ")
    c1 = int(entrada[0])
    c2 = int(entrada[1])
    d = int(entrada[2])
    grafo[c1].append((c2,d))
    grafo[c2].append((c1,d))
entrada = input("").split(" ")
s = int(entrada[0])
e = int(entrada[1])
distancias, precedencias = dijkstra(s, grafo)
print(distancias[e])
camino = []
actual = e
flag = 0
while True and not flag:
    camino.append(actual)
    if actual == s:
        flag = 1
    else:
        actual = precedencias[actual]
camino.reverse()
print(*camino)