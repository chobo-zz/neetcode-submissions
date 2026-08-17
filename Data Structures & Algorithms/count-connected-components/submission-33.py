class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
    
    def find(self, child):
        cur = child

        while self.parent[cur] != cur:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                n -= 1
        
        return n

        