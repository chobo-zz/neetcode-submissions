class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjList = defaultdict(list)

        for src, dst in tickets:
            adjList[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
        
            
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
            