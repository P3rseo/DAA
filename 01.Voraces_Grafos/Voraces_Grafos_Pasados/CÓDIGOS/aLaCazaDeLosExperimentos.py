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
        rango[ra] = rango[ra] + 1
    return True

def kruskal(grafo):
    n = len(grafo)
    aristas = []
    vistos = set()
    for i in range(n):
        for par in grafo[i]:
            j, w = par
            if i < j:
                u = i
                v = j
            else:
                u = j
                v = i
            clave = (u, v)
            if clave not in vistos:
                vistos.add(clave)
                aristas.append((w, u, v))
    aristas.sort()
    padre = []
    rango = []
    for i in range(n):
        padre.append(i)
        rango.append(0)
    total = 0
    seleccionadas = []
    numComp = n
    for i in range(len(aristas)):
        peso, nodo, vecino = aristas[i]
        if union(padre, rango, nodo, vecino):
            total += peso
            seleccionadas.append((nodo, vecino, peso))
            numComp -= 1
            if numComp == 1:
                break
    return total, seleccionadas

entrada = input("").split(" ")
n = int(entrada[0])
m = int(entrada[1])
c = int(entrada[2])
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    entrada = input("").split(" ")
    p1 = int(entrada[0])
    p2 = int(entrada[1])
    d = int(entrada[2])
    grafo[p1].append((p2, d))
    grafo[p2].append((p1, d))
listaPuntos = []
for i in range(c):
    listaPuntos.append(int(input("")))
total, seleccionadas = kruskal(grafo)
seleccionadas = sorted(seleccionadas, key=lambda x:-x[2])
print(str(len(seleccionadas)) + " " + str(total))
print(*seleccionadas[0])
while len(listaPuntos) > 0:
    punto = listaPuntos.pop(0)
    cont = 0
    for i in range(len(seleccionadas)):
        if punto == seleccionadas[i][0] or punto == seleccionadas[i][1]:
            cont += 1
    print(str(punto) + ": " + str(cont))