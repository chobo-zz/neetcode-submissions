class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r == m or c == n:
                return float("inf")
            
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            minPathSum = 0
            minPathSum = min(grid[r][c] + dfs(r + 1, c), grid[r][c] + dfs(r, c + 1))

            memo[(r, c)] = minPathSum
            return minPathSum
        
        return dfs(0, 0)