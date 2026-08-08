class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        if not grid:
            return res

        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] != "0":
                    grid[r][c] = "0"
                    q.append((r + 1, c))
                    q.append((r - 1, c))
                    q.append((r, c + 1))
                    q.append((r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)
        return res

