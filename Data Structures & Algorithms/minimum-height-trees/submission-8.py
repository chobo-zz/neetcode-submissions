class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        leaves = deque()
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        for node, degrees in indegree.items():
            if degrees == 1:
                leaves.append(node)
    
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1

                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        leaves.append(nei)
        
                

        