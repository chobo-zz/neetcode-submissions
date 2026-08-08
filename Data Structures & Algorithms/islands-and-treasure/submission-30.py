class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nc < 0 or nr < 0 or nc >= cols or nr >= rows or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = dist + 1
                q.append((nr, nc, dist + 1))
        

        

