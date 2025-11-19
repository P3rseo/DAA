import heapq

def find(padre, x):
    while padre[x] != x:
        padre[x] = padre[padre[x]]
        x = padre[x]
    return x

def union(padre, rango, a, b):
    ra = find(padre, a)
    rb = find(padre, b)
    if ra == rb:
        return False
    if rango[ra] < rango[rb]:
        ra, rb = rb, ra
    padre[rb] = ra
    if rango[ra] == rango[rb]:
        rango[ra] += 1
    return True

def kruskal(n, candidatos):
    padre = list(range(n))
    rango = [0] * n
    numComp = n
    total = 0
    aristas = []
    heapq.heapify(candidatos)
    while numComp > 1 and candidatos:
        peso, orden, nodo, vecino = heapq.heappop(candidatos)
        if union(padre, rango, nodo, vecino):
            total += peso
            aristas.append((nodo, vecino))
            numComp -= 1
    return total, aristas

entrada = input().split()
n = int(entrada[0])
m = int(entrada[1])
posiciones = []
for i in range(n):
    datos = input().split()
    x = int(datos[0])
    y = int(datos[1])
    posiciones.append((x, y))
candidatos = []
for i in range(m):
    datos = input().split()
    a = int(datos[0])
    b = int(datos[1])
    x1, y1 = posiciones[a]
    x2, y2 = posiciones[b]
    peso = abs(x1 - x2) + abs(y1 - y2)
    candidatos.append((peso, i, a, b))
total, aristas = kruskal(n, candidatos)
print(total)
for nodo, vecino in aristas:
    print(nodo, vecino)