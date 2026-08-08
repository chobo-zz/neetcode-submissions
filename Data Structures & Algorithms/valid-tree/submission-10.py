class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visiting = set()
        visited = set()
        
        def dfs(node, prev):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            visiting.remove(node)
            visited.add(node)

            return True
        
        return dfs(0, -1) and len(visited) == n
            
