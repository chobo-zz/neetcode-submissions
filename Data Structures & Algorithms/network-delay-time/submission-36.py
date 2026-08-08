class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]

        adj = defaultdict(list)
        visited = set()
        res = 0
        for u, v, t in times:
            adj[u].append((v, t))
        
        while heap and len(visited) < n:
            totalTime, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)

            res = totalTime

            for neiNode, neiTime in adj[node]:
                if neiNode not in visited:
                    heapq.heappush(heap, (neiTime + totalTime, neiNode))
        
        return res if len(visited) == n else -1

