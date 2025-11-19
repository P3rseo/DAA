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
entrada = input("").split(" ")
listaTipos = []
for i in range(n):
    listaTipos.append(int(entrada[i]))
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    entrada = input("").split(" ")
    c = int(entrada[0])
    d = int(entrada[1])
    l = int(entrada[2])
    grafo[c].append((d,l))
    grafo[d].append((c,l))
mapaTipos = {}
for i in range(n):
    componente = i
    tipo = listaTipos[i]
    if tipo not in mapaTipos:
        mapaTipos[tipo] = []
    mapaTipos[tipo].append(componente)

tiposOrdenados = sorted(mapaTipos.keys())
resultados=[]
for i in range(len(tiposOrdenados)):
    tipoActual = tiposOrdenados[i]
    nodosTipo = mapaTipos[tipoActual]
    if len(nodosTipo) < 2:
        resultados.append(-1)
        continue
    distancias = [float('inf')] * n
    origenDe = [-1] * n
    colaPrioridad = []
    for j in range(len(nodosTipo)):
        nodo = nodosTipo[j]
        distancias[nodo] = 0
        origenDe[nodo] = nodo
        heapq.heappush(colaPrioridad, (0,nodo))
    mejor = float('inf')
    while colaPrioridad:
        entradaCola = heapq.heappop(colaPrioridad)
        distanciaMin = entradaCola[0]
        nodo = entradaCola[1]
        if distanciaMin != distancias[nodo]:
            continue
        for (vecino, peso) in grafo[nodo]:
            nueva = distanciaMin + peso
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                origenDe[vecino] = origenDe[nodo]
                heapq.heappush(colaPrioridad, (nueva,vecino))
            else:
                if origenDe[vecino] != -1:
                    if origenDe[vecino] != origenDe[nodo]:
                        candidato = distanciaMin + distancias[vecino] + peso
                        if candidato < mejor:
                            mejor = candidato
    if mejor != float('inf'):
        resultados.append(mejor)
    else:
        resultados.append(-1)
print(*resultados)