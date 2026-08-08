class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topoSort(edges):
            adjList = { i: [] for i in range(1, k + 1) }
            indegree = { i: 0 for i in range(1, k + 1) }

            for u, v in edges:
                adjList[u].append(v)
                indegree[v] += 1
            
            q = deque([node for node in indegree if indegree[node] == 0])
            order = []
            
            while q:
                node = q.popleft()
                order.append(node)

                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return order if len(order) == k else []
            
        rowOrder = topoSort(rowConditions)
        if not rowOrder:
            return []
        
        colOrder = topoSort(colConditions)
        if not colOrder:
            return []
        
        rowToIndex = { v: i for i, v in enumerate(rowOrder) }
        colToIndex = { v: i for i, v in enumerate(colOrder) }
        res = [[0] * k for _ in range(k)]

        for i in range(1, k + 1):
            r, c = rowToIndex[i], colToIndex[i]
            res[r][c] = i
        
        return res

