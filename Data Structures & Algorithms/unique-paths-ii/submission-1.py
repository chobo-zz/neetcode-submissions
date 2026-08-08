class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)

            return memo[(r, c)]
        
        return dfs(0, 0)