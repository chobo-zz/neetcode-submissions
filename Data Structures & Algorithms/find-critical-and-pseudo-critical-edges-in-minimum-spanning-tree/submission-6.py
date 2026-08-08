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
    
    def union(self, p1, p2):
        p1, p2 = self.find(p1), self.find(p2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, v in enumerate(edges):
            v.append(i)
        
        edges.sort(key=lambda x: x[2])

        mstWeight = 0
        dsu = DSU(n)

        critical = []
        pseudo = []

        for u, v, w, i in edges:
            if dsu.union(u, v):
                mstWeight += w
        
        for u, v, w, i in edges:
            dsu = DSU(n)

            weight = 0
            for u2, v2, w2, i2 in edges:
                if i2 != i and dsu.union(u2, v2):
                    weight += w2
            
            if max(dsu.rank) != n or weight > mstWeight:
                critical.append(i)
                continue
            
            dsu = DSU(n)
            dsu.union(u, v)
            weight = w
            for u3, v3, w3, i3 in edges:
                if dsu.union(u3, v3):
                    weight += w3
            
            if max(dsu.rank) == n and weight == mstWeight:
                pseudo.append(i)
        
        return [critical, pseudo]
        
        