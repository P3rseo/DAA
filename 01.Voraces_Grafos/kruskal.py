def sort_aristas(g):
    aristas = []
    for adj in g:
        for src, dst, w in adj:
            aristas.append((w, src, dst))
    aristas.sort()
    return aristas

def update_components(componentes, nuevo_id, viejo_id):
    for i in range(len(componentes)):
        if componentes[i] == viejo_id:
            componentes[i] = nuevo_id

def kruskal(g):
    aristas = sort_aristas(g)
    compConex = list(range(len(g)))
    numCompConex = len(compConex)
    valor = 0
    indice = 0

    while indice < len(aristas) and numCompConex > 1:
        w, src, dst = aristas[indice]
        if compConex[src] != compConex[dst]:
            update_components(compConex, compConex[src], compConex[dst])
            valor += w
            numCompConex -= 1
        indice += 1

    return valor

g = [
    [],
    [(1,3,1), (1,4,2), (1,7,6)],
    [(2,5,2), (2,6,4), (2,7,7)],
    [(3,1,1), (3,4,3), (3,7,5)],
    [(4,1,2), (4,3,3), (4,5,1), (4,6,9)],
    [(5,2,2), (5,4,1), (5,7,8)],
    [(6,2,4), (6,4,9)],
    [(7,1,6), (7,2,7), (7,3,5), (7,5,8)]
]

sol = kruskal(g)
print(sol)