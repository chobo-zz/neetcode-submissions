class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)] # distance, node
        visited = set()
        runningCost = 0

        adj = defaultdict(list) # node -> (distance, otherNode)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        while heap:
            dist, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            runningCost += dist

            for distance, neighbor in adj[node]:
                heapq.heappush(heap, (distance, neighbor))
        
        return runningCost
            
            