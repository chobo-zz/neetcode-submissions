class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        q = deque()
        visited = set()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        while q:
            r, c, d = q.popleft()
            
            
            grid[r][c] = d

            for dr, dc in directions:
                nr, nc, nd = r + dr, c + dc, d + 1
                if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr, nc) in visited or grid[nr][nc] != 2147483647:
                    continue
                visited.add((nr, nc))
                q.append((nr, nc, nd))
        
    


