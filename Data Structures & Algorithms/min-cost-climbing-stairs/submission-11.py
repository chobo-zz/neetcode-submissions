class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {} # minimum cost to reach last step from here (i -> cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i + 2), dfs(i + 1))
            return memo[i]

        return min(dfs(0), dfs(1))
