class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 ] * n for _ in range(m)] # stores unique paths to end from that cell

        def dfs(i, j): # returns how many unique paths to end from this cell
            if i == (m - 1) and j == (n - 1):
                return 1
            
            if i >= m or j >= n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            res = dfs(i + 1, j) + dfs(i, j + 1)

            memo[i][j] = res
            return res
        
        return dfs(0, 0)

