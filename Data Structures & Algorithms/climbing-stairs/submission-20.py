class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i): # num ways to reach i
            if i < 0:
                return 0
            if i == 0:
                return 1
            if i in memo:
                return memo[i]

            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i] 
        
        return dfs(n)
