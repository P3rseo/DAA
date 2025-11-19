def sort_candidates(g):
    candidates = []
    for adj in g:
        for src, dst, cost in adj:
            candidates.append((cost, src, dst))
    candidates.sort()
    return candidates

def update_components(componentes, nuevo_id, viejo_id):
    for i in range(len(componentes)):
        if componentes[i] == viejo_id:
            componentes[i] = nuevo_id

def kruskal(g):
    aristas = sort_candidates(g)
    compConex = list(range(len(g)))
    numCompConex = len(compConex)
    valor = 0
    indice = 0
    empleados = [0] * numCompConex

    while indice < len(aristas) and numCompConex > 1:
        cost, src, dst = aristas[indice]
        if compConex[src] != compConex[dst]:
            empleados[src] += 1
            empleados[dst] += 1
            update_components(compConex, compConex[src], compConex[dst])
            valor += cost
            numCompConex -= 1
        indice += 1

    return valor, empleados

numPuntos, numPosiblesConexiones = map(int, input().strip().split())
g = [[] for _ in range(numPuntos)]

for i in range(numPosiblesConexiones):
    src, dst, cost = map(int, input().strip().split())
    g[src].append((src, dst, cost))
    g[dst].append((dst, src, cost))

valor, empleados = kruskal(g)
print(valor)
print(*empleados)