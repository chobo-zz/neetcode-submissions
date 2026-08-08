class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i:[] for i in range(n)}
        res = 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for n in adj[node]:
                dfs(n)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res

