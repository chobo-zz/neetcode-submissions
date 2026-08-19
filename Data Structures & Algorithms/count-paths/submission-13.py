class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            
            if x >= m or y >= n:
                return 0
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            res = 0
            res += dfs(x + 1, y)
            res += dfs(x, y + 1)
            memo[(x, y)] = res
            return res
        
        return dfs(0, 0)