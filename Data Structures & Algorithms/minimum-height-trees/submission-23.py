class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, prev):
            height = 0

            for nei in adjList[node]:
                if nei != prev:
                    height = max(height, 1 + dfs(nei, node))
            
            return height
        
        minHeight = n
        for i in range(n):
            height = dfs(i, -1)
            if height < minHeight:
                minHeight = height
                res = [i]
            elif height == minHeight:
                res.append(i)
        return res