class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        
        heap = [(0, 0)] # distance, point
        visited = set()
        
        minCost = 0
        while heap:
            dist, point = heapq.heappop(heap)

            if point in visited:
                continue
            visited.add(point)
            minCost += dist

            for nPoint, nDist in adj[point]:
                if nPoint not in visited:
                    heapq.heappush(heap, (nDist, nPoint))
        
        return minCost
            
