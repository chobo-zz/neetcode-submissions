class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = { i: [] for i in range(n) }

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)
            
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count