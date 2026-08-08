class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} # num ways to reach end starting from index i (i -> num ways)

        def dfs(i): # returns num ways to reach end starting from this index
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)