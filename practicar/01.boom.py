import heapq

def dijkstra(g, start):
    n = len(g)

    distances = [float('inf')] * n
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        if current_dist > distances[u]:
            continue
            
        for _, v, w in g[u]:
            new_dist = current_dist + w

            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    
    return distances


numComponentes, numConexiones = map(int, input().strip().split())
tipoComponente = list(map(int, input().strip().split()))

conexiones = [[] for _ in range(numComponentes)]

for _ in range(numConexiones):
    c1, c2, l = map(int, input().strip().split())
    conexiones[c1].append((c1, c2, l))
    conexiones[c2].append((c2, c1, l))

distances = dijkstra(conexiones, 0)
print(distances)

