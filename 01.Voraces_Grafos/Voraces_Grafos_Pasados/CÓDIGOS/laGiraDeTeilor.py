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
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    entrada = input("").split(" ")
    c1 = int(entrada[0])
    c2 = int(entrada[1])
    f = int(entrada[2])
    grafo[c1].append((c2, f))
    grafo[c2].append((c1, f))
total, seleccionadas = kruskal(grafo)
print("Fuerzas desplegadas: " + str(total))
mapaFuerzas = {}
for i in range(n):
    mapaFuerzas[i] = 0
for i in range(len(seleccionadas)):
    nodo, vecino, peso = seleccionadas[i]
    mapaFuerzas[nodo] += peso
    mapaFuerzas[vecino] += peso
media = total / n
ciudadesOrdenadas = sorted(mapaFuerzas.keys())
menosProblematicas = []
for i in ciudadesOrdenadas:
    if mapaFuerzas[i] < media:
        menosProblematicas.append(i)
print(*menosProblematicas)