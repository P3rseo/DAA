import heapq


def dijkstra(g, start):
    """
    Calcula las distancias mínimas desde el nodo start
    hasta todos los demás nodos usando Dijkstra.

    Complejidad:
        O((V + E) log V)
    """

    n = len(g) - 1

    # Distancias mínimas conocidas
    distances = [float('inf')] * (n + 1)
    distances[start] = 0

    # Cola de prioridad: (distancia, nodo)
    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        # Ignorar entradas obsoletas
        if current_dist > distances[u]:
            continue

        # Relajar aristas salientes
        for _, v, w in g[u]:
            new_dist = current_dist + w

            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return distances


# ======================
# PRUEBA
# ======================

g = [
    [],
    [(1, 2, 5), (1, 4, 3)],
    [(2, 5, 1)],
    [],
    [(4, 2, 1), (4, 3, 11), (4, 5, 6)],
    [(5, 3, 1)]
]

start = 1

distances = dijkstra(g, start)

print("Distancias mínimas desde el nodo", start)
for node in range(1, len(g)):
    print(f"{start} -> {node}: {distances[node]}")