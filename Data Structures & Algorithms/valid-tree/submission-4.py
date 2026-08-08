class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(n) }

        visited = set()

        for u, v in edges:
            preMap[u].append(v)
            preMap[v].append(u)

        
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in preMap[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            
            return True

        
        return dfs(0, -1) and len(visited) == n