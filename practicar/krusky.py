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

    for u in range(1, len(g)):
        for _, v, w in g[u]:
            if u < v:
                edges.append((w, u, v))
            
        edges.sort()

        uf = UnionFind(len(g))

        total = 0

        for w, u, v in edges:
            if uf.union(u, v):
                total += w
        
        return total
    