class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        indegree = [0] * n
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque([i for i in range(n) if indegree[i] == 1])

        while q:
            if n <= 2:
                return list(q)
                
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
        

