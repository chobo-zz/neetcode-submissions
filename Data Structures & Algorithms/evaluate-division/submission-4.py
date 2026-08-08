class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i, eq in enumerate(equations):
            x, y = eq
            adjList[x].append((y, values[i]))
            adjList[y].append((x, 1 / values[i]))
        
        def bfs(src, target):
            if src not in adjList or target not in adjList:
                return -1
            queue, visited = deque([(x, 1)]), set([x])
            while queue:
                node, weight = queue.popleft()

                if node == target:
                    return weight
                
                for nei, neiWeight in adjList[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, weight * neiWeight))
            return -1
                
        
        res = []
        for query in queries:
            x, y = query
            queryResult = bfs(x, y)
            res.append(queryResult)
        return res