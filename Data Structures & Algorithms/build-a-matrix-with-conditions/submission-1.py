class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, adjList, visited, visiting, order):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)
            for nei in adjList[node]:
                if not dfs(nei, adjList, visited, visiting, order):
                    return False
            visiting.remove(node)
            visited.add(node)
            order.append(node)
            return True

        def topoSort(edges):
            adjList = defaultdict(list)
            for u, v in edges:
                adjList[u].append(v)
            
            order = []
            visited = set()
            visiting = set()

            for node in range(1, k + 1):
                if not dfs(node, adjList, visited, visiting, order):
                    return []
            return order[::-1]

        rowOrder = topoSort(rowConditions)
        if not rowOrder:
            return []
        
        colOrder = topoSort(colConditions)
        if not colOrder:
            return []
        
        rowToIndex = {v: i for i, v in enumerate(rowOrder)}
        colToIndex = {v: i for i, v in enumerate(colOrder)}
        res = [[0] * k for _ in range(k)]

        for i in range(1, k + 1):
            row = rowToIndex[i]
            col = colToIndex[i]
            res[row][col] = i
        return res
