class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited, visiting = set(), set()
        def dfs(i, prev):
            if i in visiting:
                return False
            
            if i in visited:
                return True
            
            visiting.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            
            visiting.remove(i)
            visited.add(i)
            return True
        
        return dfs(0, -1) and len(visited) == n