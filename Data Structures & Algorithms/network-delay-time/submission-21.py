class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        res = 0

        for u, v, t in times:
            adj[u].append((v, t))
        
        heap = [(0, k)]
        visited = set()

        while heap:
            curTime, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res = curTime
            for v, t in adj[node]:
                if v not in visited:
                    heapq.heappush(heap, (curTime + t, v))
        
        return res if len(visited) == n else -1
