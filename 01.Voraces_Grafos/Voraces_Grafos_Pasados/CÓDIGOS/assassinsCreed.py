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
for i in range(n):
    grafo.append([])
for i in range(m):
    entrada = input("").split(" ")
    o = int(entrada[0])
    d = int(entrada[1])
    m = int(entrada[2])
    grafo[o].append((d, m))
    grafo[d].append((o, m))
r = int(input(""))
entrada = input("").split(" ")
zonasPago = []
for i in range(len(entrada)):
    zonasPago.append(entrada[i])
entrada = input("").split(" ")
x = int(entrada[0])
y = int(entrada[1])
if x in zonasPago or y in zonasPago:
    print("IMPOSIBLE")
else:
    grafoFiltrado = []
    for i in range(n):
        grafoFiltrado.append([])
    permitidos = []
    for i in range(n):
        if i in zonasPago:
            permitidos.append(False)
        else:
            permitidos.append(True)
    for i in range(n):
        if permitidos[i] == False:
            continue
        for par in grafo[i]:
            vecino = par[0]
            peso = par[1]
            if permitidos[vecino] == True:
                grafoFiltrado[i].append((vecino, peso))
    distancias, precedencias = dijkstra(x, grafoFiltrado)
    if distancias[y] == float('inf'):
        print("IMPOSIBLE")
    else:
        print(distancias[y])