import heapq

def dijkstra(origen, grafo):
    n = len(grafo)
    distancias = [float('inf')] * n
    distancias[origen] = 0
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
                heapq.heappush(colaPrioridad, (distancias[vecino], vecino))
    return distancias

entrada = input("").split(" ")
n = int(entrada[0])
m = int(entrada[1])
t = int(entrada[2])
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    entrada = input("").split(" ")
    h_1 = int(entrada[0])
    h_2 = int(entrada[1])
    d = int(entrada[2])
    grafo[h_1].append((h_2, d))
    grafo[h_2].append((h_1, d))
distancias=dijkstra(0, grafo)
tiempoTotal = 0
for i in range(len(distancias)):
    if i != 0 and distancias[i] < float('inf'):
        tiempoTotal += distancias[i]
if tiempoTotal <= t:
    print(tiempoTotal)
else:
    print("Aleg, ¡a decorar!")
