class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, child):
        cur = child
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, v in edges:
            if dsu.union(u, v):
                continue
            return [u, v]