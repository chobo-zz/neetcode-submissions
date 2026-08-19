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
        
        def topSort(conditions):
            adjList = defaultdict(list)

            for u, v in conditions:
                adjList[u].append(v)
            
            visited = set()
            visiting = set()
            order = []
            for i in range(1, k + 1):
                if not dfs(i, adjList, visited, visiting, order):
                    return []
            order.reverse()
            return order

        rowOrder = topSort(rowConditions)
        if not rowOrder:
            return []

        colOrder = topSort(colConditions)
        if not colOrder:
            return []

        res = [[0] * k for _ in range(k)]
        rowToIndex = {v: i for i, v in enumerate(rowOrder)}
        colToIndex = {v: i for i, v in enumerate(colOrder)}

        for i in range(1, k + 1):
            rowIndex, colIndex = rowToIndex[i], colToIndex[i]
            res[rowIndex][colIndex] = i
        
        return res
