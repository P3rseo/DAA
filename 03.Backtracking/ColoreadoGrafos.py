def is_solution(k, g):
    #return (-1 not in sol)
    return k == len(g)

def is_factible(g, sol, k, color):
    factible = True
    i = 0
    while i < len(g[k]) and factible:
        vecino = g[k][i]
        if vecino < k:
            factible = (sol[vecino] != color)
        else:
            return factible
        i += 1

    return factible


def graph_coloring_bt(g, m, k, sol):
    if is_solution(k, g):
        is_sol = True
    else:
        color = 1
        is_sol = False
        while color <= m and not is_sol:
            if is_factible(g, sol, k, color):
                sol[k] = color
                sol, is_sol = graph_coloring_bt(g, m, k+1, sol)
                if not is_sol:
                    sol[k] = -1

            color += 1

    return sol, is_sol


g = [
    [1,2,3],
    [0],
    [0,3],
    [0,2]
]

m = 3 # Numero maximo de colores
inicial = 0 # Nodo inicial
sol = [-1] * len(g) # Solucion inicial a -1
sol, es_sol = graph_coloring_bt(g, m, inicial, sol)
if es_sol:
    print(sol)
else:
    print("No hay solucion")