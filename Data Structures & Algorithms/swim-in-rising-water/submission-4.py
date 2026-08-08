class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # use dijkstra's algorithm since we need to choose shortest path 
        # based on heights (grid cell value act as the weighted edge)
        # use a min heap to efficiently get the lowest weighted edge for traversal
        # minHeap = [maxHeightSoFar, xCoordinate, yCoordinate]

        N = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            height, x, y = heapq.heappop(minHeap)

            if x == N - 1 and y == N - 1:
                return height
            
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= N or (nx, ny) in visited:
                    continue
                heapq.heappush(minHeap, [max(height, grid[nx][ny]), nx, ny])
                visited.add((x, y))