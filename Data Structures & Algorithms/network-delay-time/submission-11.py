class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        heap = [(0, k)]
        visited = set()
        totalTime = 0

        while heap:
            curTime, curNode = heapq.heappop(heap)

            if curNode in visited:
                continue
            
            visited.add(curNode)
            totalTime = max(totalTime, curTime)

            for nei, neiTime in adj[curNode]:
                if nei not in visited:
                    heapq.heappush(heap, (curTime + neiTime, nei))
        
        return totalTime if len(visited) == n else -1
