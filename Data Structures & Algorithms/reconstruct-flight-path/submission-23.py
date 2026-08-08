class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjList = defaultdict(list)
        res = ["JFK"]

        for src, dst in sorted(tickets):
            adjList[src].append(dst)

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in adjList:
                return False
            
            temp = list(adjList[src])
            for i, v in enumerate(temp):
                res.append(v)
                adjList[src].pop(i)
                if dfs(v):
                    return True
                res.pop()
                adjList[src].insert(i, v)
            return False
        
        dfs("JFK")
        return res