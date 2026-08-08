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
        
        heap = [(0, 0)] # distance, node
        visited = set()
        res = 0

        while heap:
            distance, node = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)
            res += distance

            for neighbor, distance in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (distance, neighbor))
        return res
            
                

