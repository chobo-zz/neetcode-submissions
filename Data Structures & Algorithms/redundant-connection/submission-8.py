class DSU:
    def __init__(self, n):
        self.parent = { i : i for i in range(n + 1) }
        self.rank = { i: 1 for i in range(n + 1) }

    def find(self, node):
        cur = node

        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False
        
        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
            self.rank[u] += self.rank[v]
        else:
            self.parent[u] = self.parent[v]
            self.rank[v] += self.rank[u]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        numOfNodes = len(edges)
        dsu = DSU(numOfNodes)

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]

        