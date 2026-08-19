class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return 1
            
            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = dfs(r + 1, c) + dfs(r, c + 1)
            memo[(r, c)] = res
            return res
        
        return dfs(0, 0)