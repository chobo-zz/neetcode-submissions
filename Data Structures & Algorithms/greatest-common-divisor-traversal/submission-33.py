class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.size = n
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
        self.size -= 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        dsu = DSU(len(nums))
        factorToIndex = defaultdict(int)

        for i, v in enumerate(nums):
            f = 2

            while f * f <= v:
                if v % f == 0:
                    if f in factorToIndex:
                        dsu.union(i, factorToIndex[f])
                    else:
                        factorToIndex[f] = i
                
                    while v % f == 0:
                        v = v // f
                f += 1
            
            if v > 1:
                if v in factorToIndex:
                    dsu.union(i, factorToIndex[v])
                else:
                    factorToIndex[v] = i


        return dsu.size == 1