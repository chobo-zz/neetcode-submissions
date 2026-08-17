class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        visiting = set()
        def dfs(node, prev):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)
            for nei in adjList[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        return dfs(0, -1) and len(visited) == n