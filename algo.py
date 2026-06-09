# --- BUSQUEDA BINARIA --------------------------------------------
def binary_search(lista, buscado, inferior, superior):
    if inferior > superior:
        return -1
    else:
        mitad = (inferior + superior) // 2

        if lista[mitad] == buscado:
            return mitad
        elif lista[mitad] < buscado:
            return binary_search(lista, buscado, inferior, mitad-1)
        else:
            return binary_search(lista, buscado, mitad+1, superior)
# -----------------------------------------------------------------

# --- MERGE SORT --------------------------------------------------
def merge(list, left, right):
    l = 0
    r = 0
    i = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            list[i] = left[l]
            l += 1
        else:
            list[i] = right[r]
            r += 1
        i += 1

    if l < len(left):
        resto = left
        f = l
    else:
        resto = right
        f = r
    
    for j in range(f, len(resto)):
        list[i] = resto[j]
        i += 1

def merge_sort(list):
    if len(list) == 1:
        return list
    
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(list, left, right)
# -----------------------------------------------------------------
"""
# --- KRUSKAL -----------------------------------------------------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    def union(self, a, b):
        root_a = self.find[a]
        root_b = self.find[b]

        if root_a == root_b:
            return False
        
        self.parent[root_b] = root_a
        return True

def kruskal(g):
    edges = []

    for u in range(1, len(g)):
        for _, v, w in g[u]:
            edges.append((w, u, v))
    
    edges.sort()
    uf = UnionFind(len(g))
    total = 0

    for w, u, v in edges:
        if uf.union(u, v):
            total += w

    return total
# -----------------------------------------------------------------
"""
# --- DIJKSTRA ----------------------------------------------------
import heapq

def dijkstra(g, start):
    n = len(g) - 1
    distances = [float('inf')] * (n+1)
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
# -----------------------------------------------------------------

lista = [4,6,2,4,2,1,6,8,89,5,424,678,785,7,8567,85,67]
otra = [1,2,3,4,5,6,7,8,9,10]
