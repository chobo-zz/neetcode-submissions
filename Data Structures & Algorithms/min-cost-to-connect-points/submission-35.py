class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        heap = [(0, 0)]
        visited = set()
        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        
        res = 0
        while heap and len(visited) < len(points):
            dist, point = heapq.heappop(heap)

            if point in visited:
                continue
            
            visited.add(point)
            res += dist

            for neiPoint, neiDist in adj[point]:
                if neiPoint not in visited:
                    heapq.heappush(heap, (neiDist, neiPoint))
        
        return res
