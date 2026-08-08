class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, prev):
            height = 1
            for nei in adjList[node]:
                if nei == prev:
                    continue
                height = max(height, 1 + dfs(nei, node))
            return height
                
        
        minHeight = n
        res = []
        for node in range(n):
            height = dfs(node, -1)
            if height == minHeight:
                res.append(node)
            elif height < minHeight:
                minHeight = height
                res = [node]
        return res