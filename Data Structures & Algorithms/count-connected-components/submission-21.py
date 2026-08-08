class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, child):
        cur = child
        
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
            self.parent[u] = v
            self.rank[v] += self.rank[u]
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        count = n
        for u, v in edges:
            if dsu.union(u, v):
                count -= 1
        return count
                
        