class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            height, x, y = heapq.heappop(heap)

            if x == n - 1 and y == n - 1:
                return height

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                heapq.heappush(heap, (max(height, grid[nx][ny]), nx, ny))

