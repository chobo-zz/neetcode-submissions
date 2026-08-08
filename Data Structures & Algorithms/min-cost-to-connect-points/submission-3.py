class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's algorithm to find minimum spanning tree
        # use minHeap to always get lowest cost distance 
        # use set to ensure we never revisit nodes

        # build adjacency list both ways (adj[i] = [distance, otherNode])

        adj = collections.defaultdict(list)

        for i in range(len(points)):
            x, y = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                distance = abs(x - x2) + abs(y - y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        
        minHeap = [[0, 0]] # for prim's algorithm, we can start from any node, so we just choose node at index 0
        res = 0
        visited = set()

        while minHeap:
            # heap pop will always get minimum distance, so we can immediately add distance to result
            distance, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res += distance

            for distance, otherNode in adj[node]:
               
                heapq.heappush(minHeap, [distance, otherNode])

        return res

        
