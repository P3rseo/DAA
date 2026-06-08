class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        self.parent[root_b] = root_a
        return True
    
def kruskal(g):
    edges = []

    for u in range(0, len(g)):
        for _, v, d in g[u]:
            if u < v:
                edges.append((d, u, v))
        
    edges.sort()
    uf = UnionFind(len(g))
    totalMetros = 0
    aristasUsadas = 0

    for d, u, v in edges:
        if uf.union(u, v):
            totalMetros += d
            if aristasUsadas == len(g)-1:
                break

    return (totalMetros + 4) // 5



numPuestosSeguros, numConexionesTotal = map(int, input().strip().split())

grafo = [[] for i in range(numPuestosSeguros)]
for _ in range(numConexionesTotal):
    n1, n2, d = map(int, input().strip().split())
    grafo[n1].append((n1, n2, d))
    grafo[n2].append((n2, n1, d))


totalMetros = kruskal(grafo)
print(totalMetros)

