class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))

        emailsToAcc = defaultdict(int) # email -> account Id (index from accounts list)

        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailsToAcc:
                    dsu.union(index, emailsToAcc[email])
                else:
                    emailsToAcc[email] = index
        
        emailsGroup = defaultdict(list)
        for email in emailsToAcc:
            leader = dsu.find(emailsToAcc[email])
            emailsGroup[leader].append(email)
        
        res = []
        for leader, emailGroup in emailsGroup.items():
            name = accounts[leader][0]
            subres = [name] + sorted(emailGroup)
            res.append(subres)
        return res
        
        