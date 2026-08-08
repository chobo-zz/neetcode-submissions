class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        visited = set()
        heap = [(0, k)] # total weight, node

        res = 0
        while heap:
            totalWeight, node = heapq.heappop(heap)
            if node in visited:
                continue
            res = max(res, totalWeight)
            visited.add(node)
            for neighbor, weight in adj[node]:
                heapq.heappush(heap, (totalWeight + weight, neighbor))
        
        return res if len(visited) == n else -1
                

            