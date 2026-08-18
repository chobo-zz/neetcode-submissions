class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        res = []
        for src, dst in sorted(tickets)[::-1]:
            adjList[src].append(dst)


        def dfs(ticket):
            while adjList[ticket]:
                dest = adjList[ticket].pop()
                dfs(dest)
            res.append(ticket)
        
        dfs("JFK")
        res.reverse()
        return res
        