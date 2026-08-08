class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for index, equation in enumerate(equations):
            x, y = equation
            adjList[x].append((y, values[index]))
            adjList[y].append((x, 1 / values[index]))
        
        def bfs(src, target):
            if src not in adjList or target not in adjList:
                return -1
                        
            q = deque([(src, 1)])
            visited = set([src])

            while q:
                node, weight = q.popleft()

                if node == target:
                    return weight
                
                for nei, neiWeight in adjList[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, weight * neiWeight))
            return -1
        
        return [bfs(x, y) for x, y in queries]
                