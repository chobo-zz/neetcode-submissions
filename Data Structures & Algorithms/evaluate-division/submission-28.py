class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            adjList[x].append((y, value))
            adjList[y].append((x, 1 / value))
        
        def bfs(src, dst, visited):
            if src not in adjList or dst not in adjList:
                return -1
            
            q = deque([(src, 1)])

            while q:
                node, weight = q.popleft()
                if node == dst:
                    return weight
                
                for nei, neiWeight in adjList[node]:
                    if nei not in visited:
                        q.append((nei, weight * neiWeight))
                        visited.add(nei)
            return -1
            

        return [bfs(x, y, set()) for x, y in queries]
