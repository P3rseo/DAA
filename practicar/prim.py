import heapq


# =========================
# PRIM CON HEAPQ
# =========================

def prim(g, start=1):
    n = len(g)
    visited = [False] * n
    heap = []
    total_cost = 0
    edges_used = 0

    visited[start] = True

    for _, end, weight in g[start]:
        heapq.heappush(heap, (weight, start, end))

    while heap and edges_used < n - 2:
        weight, origin, node = heapq.heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        total_cost += weight
        edges_used += 1

        for _, end, w in g[node]:
            if not visited[end]:
                heapq.heappush(heap, (w, node, end))

    return total_cost

g = [
    [],
    [(1, 3, 1), (1, 4, 2), (1, 7, 6)],
    [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
    [(3, 1, 1), (3, 4, 3), (3, 7, 5)],
    [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
    [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
    [(6, 2, 4), (6, 4, 9)],
    [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)]
]

print("Prim:", prim(g))