class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)] # cost, x, y
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while heap:
            cost, x, y = heapq.heappop(heap)

            if x == rows - 1 and y == cols - 1:
                return cost

            if (x, y) in visited:
                continue
            
            visited.add((x, y))

            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited:
                    continue
                heapq.heappush(heap, (max(cost, grid[nr][nc]), nr, nc))


        