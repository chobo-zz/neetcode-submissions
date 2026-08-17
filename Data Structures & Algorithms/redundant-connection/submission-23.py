class DSU:
    def __init__(self, n):
        self.rank = [1] * (n + 1)
        self.parent = [i for i in range( n + 1)]
    
    def find(self, child):
        while child != self.parent[child]:
            self.parent[child] = self.parent[self.parent[child]]
            child = self.parent[child]
        
        return child

    def union(self, p1, p2):
        p1, p2 = self.find(p1), self.find(p2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]