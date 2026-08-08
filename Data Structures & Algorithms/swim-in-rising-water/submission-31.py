class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while heap:
            totalTime, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return totalTime

            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited:
                    continue
                heapq.heappush(heap, (max(totalTime, grid[nr][nc]), nr, nc))
        


