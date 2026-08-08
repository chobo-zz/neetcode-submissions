class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                nr, nc, nd = r + dr, c + dc, dist + 1
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = nd
                q.append((nr, nc, nd))
            
                    
            