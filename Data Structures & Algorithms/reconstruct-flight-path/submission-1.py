class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # hierholzer's algorithm: traverse all edges first, then add node to res when no edges left
        # this computes our res list in reverse order, just return the reverse of that array as the ans
        # must also sort the input tickets list (for lexographic comparison)

        res = []

        # build adjacency list:
        adj = collections.defaultdict(list)

        # we process the sorted list in reverse order so we can use pop() later
        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)
        
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()
                dfs(dest)
            res.append(src)

        dfs("JFK")
        return res[::-1]
        


