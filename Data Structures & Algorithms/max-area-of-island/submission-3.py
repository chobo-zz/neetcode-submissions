class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        res = 0

        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0

            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))


        for r in range(rows):
            for c in range (cols):
                res = max(res, dfs(r, c))

        return res
