class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        tickets.sort(reverse=True)

        for src, dst in tickets:
            adjList[src].append(dst)
        
        def dfs(src):
            while adjList[src]:
                dst = adjList[src].pop()
                dfs(dst)
            res.append(src)

        res = []
        dfs("JFK")
        return res[::-1]
        