class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.size = n
    
    def find(self, child):
        cur = child
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self, p1, p2):
        p1, p2 = self.find(p1), self.find(p2)

        if p1 == p2:
            return
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.size -= 1
    
    def isConnected(self):
        return self.size == 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        dsu = DSU(len(nums))

        factorToIndex = {}

        for i in range(len(nums)):
            # find prime factors of each number and map it to the number's index position
            f = 2
            n = nums[i]
            while f * f <= n:
                if n % f == 0:
                    if f in factorToIndex:
                        dsu.union(i, factorToIndex[f])
                    else:
                        factorToIndex[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            
            # also check n itself is a prime factor after removing its other factors
            if n > 1:
                if n in factorToIndex:
                    dsu.union(i, factorToIndex[n])
                else:
                    factorToIndex[n] = i
        
        return dsu.isConnected()



