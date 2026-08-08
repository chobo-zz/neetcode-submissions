class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adjList = defaultdict(list)
        res = []
        for src, dst in tickets:
            adjList[src].append(dst)
        
        def dfs(src):
            while adjList[src]:
                dst = adjList[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]