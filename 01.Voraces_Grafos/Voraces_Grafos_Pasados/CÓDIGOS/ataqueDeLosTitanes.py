import heapq
import math

def prim(grafo):
    n = len(grafo)
    visitados = [False] * n
    colaPrioridad = []
    visitados[0] = True
    for vecino, peso in grafo[0]:
        heapq.heappush(colaPrioridad, (peso, 0, vecino))
    total = 0
    cont = 1
    while colaPrioridad and cont < n:
        peso, inicio, fin = heapq.heappop(colaPrioridad)
        if visitados[fin]:
            continue
        visitados[fin] = True
        total += peso
        cont += 1
        for nuevoFin, nuevoPeso in grafo[fin]:
            if not visitados[nuevoFin]:
                heapq.heappush(colaPrioridad, (nuevoPeso, fin, nuevoFin))
    return total

entrada = input("").split(" ")
n = int(entrada[0])
m = int(entrada[1])
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    entrada = input("").split(" ")
    n1 = int(entrada[0])
    n2 = int(entrada[1])
    d = int(entrada[2])
    grafo[n1].append((n2, d))
    grafo[n2].append((n1, d))
print(math.ceil(prim(grafo)/5))