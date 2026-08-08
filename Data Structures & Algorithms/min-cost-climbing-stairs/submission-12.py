class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0: 0, 1: 0}  # cost to reach step i

        def dfs(i):
            if i in memo:
                return memo[i]
            
            memo[i] = min(
                dfs(i - 1) + cost[i - 1],
                dfs(i - 2) + cost[i - 2]
            )
            return memo[i]

        return dfs(len(cost))  # reaching the "top"