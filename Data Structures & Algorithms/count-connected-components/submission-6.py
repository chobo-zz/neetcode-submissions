class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i:[] for i in range(n)}
        res = 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)

            for n in adj[node]:
                if n != prev:   
                    dfs(n, node)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1

        return res

