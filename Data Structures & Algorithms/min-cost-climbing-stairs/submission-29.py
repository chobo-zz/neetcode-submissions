class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {} # (i -> min cost to reach end starting from i)

        def dfs(i): # returns min cost to reach end starting from i
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
        
        return min(dfs(0), dfs(1))