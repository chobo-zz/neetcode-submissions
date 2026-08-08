class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        totalTime = 0
        fresh = 0
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        
        while q:
            r, c, curTime = q.popleft()

            for dr, dc in directions:
                nr, nc, newTime  = r + dr, c + dc, curTime + 1
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                fresh -= 1
                totalTime = max(newTime, totalTime)
                q.append((nr, nc, newTime))
        
        return totalTime if fresh == 0 else -1
        


