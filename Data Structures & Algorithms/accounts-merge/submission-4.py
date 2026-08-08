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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        
        emailToAcc = defaultdict(int)
        res = []

        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    dsu.union(index, emailToAcc[email])
                else:
                    emailToAcc[email] = index
        
        emailGroup = defaultdict(list)
        for email in emailToAcc:
            leader = dsu.find(emailToAcc[email])
            emailGroup[leader].append(email)
        
        for leader, emails in emailGroup.items():
            name = accounts[leader][0]
            res.append([name] + sorted(emails))
        
        return res


            
        
