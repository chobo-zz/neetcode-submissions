class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)

        res = []
        
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()
                dfs(dest)
            res.append(src)
        
        dfs("JFK")

        return res[::-1]