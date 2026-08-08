class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            curHeight, x, y = heapq.heappop(heap)

            if x == rows - 1 and y == cols - 1:
                return curHeight
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                newHeight = grid[nx][ny]
                heapq.heappush(heap, (max(curHeight, newHeight), nx, ny))
        