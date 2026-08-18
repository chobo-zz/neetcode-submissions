class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)

                adjList[i].append((j, dist))
                adjList[j].append((i, dist))
        
        heap = [(0, 0)]
        visited = set()

        totalDistance = 0
        while heap and len(visited) < len(points):
            dist, point = heapq.heappop(heap)

            if point in visited:
                continue
            visited.add(point)

            totalDistance += dist

            for nei, neiDist in adjList[point]:
                if nei not in visited:
                    heapq.heappush(heap, (neiDist, nei))
        
        return totalDistance
            