class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} # i -> ways to reach n

        def dfs(step):
            if step > n:
                return 0
            if step == n:
                return 1
            if step in memo:
                return memo[step]
            
            memo[step] = dfs(step + 1) + dfs(step + 2)
            return memo[step]
        
        return dfs(0)