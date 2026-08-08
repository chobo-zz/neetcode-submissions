class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topSort(conditions):
            adjList = defaultdict(list)
            indegree = { i: 0 for i in range(1, k + 1) }

            for u, v in conditions:
                adjList[u].append(v)
                indegree[v] += 1
            
            q = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            res = []
            while q:
                node = q.popleft()
            
                res.append(node)
                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return res if len(res) == len(indegree) else []

        
        rowOrder = topSort(rowConditions)
        if not rowOrder:
            return []
        
        colOrder = topSort(colConditions)
        if not colOrder:
            return []
        
        rowToIndex = { v: i for i, v in enumerate(rowOrder) }
        colToIndex = { v: i for i, v in enumerate(colOrder) }

        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            r, c = rowToIndex[i], colToIndex[i]
            res[r][c] = i

        return res

        