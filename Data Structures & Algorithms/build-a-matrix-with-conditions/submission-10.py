class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, visiting, visited, order, adjList):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)
            
            for nei in adjList[node]:
                if not dfs(nei, visiting, visited, order, adjList):
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
                if not dfs(i, visiting, visited, order, adjList):
                    return []
            return order[::-1]                
        
        rowOrder = topSort(rowConditions)
        if not rowOrder:
            return []
        
        colOrder = topSort(colConditions)
        if not colOrder:
            return []

        rowToIndex = {v: i for i, v in enumerate(rowOrder)}
        colToIndex = {v: i for i, v in enumerate(colOrder)}


        res = [[0] * k for _ in range(k)]

        for i in range(1, k + 1):
            r, c = rowToIndex[i], colToIndex[i]
            res[r][c] = i

        return res