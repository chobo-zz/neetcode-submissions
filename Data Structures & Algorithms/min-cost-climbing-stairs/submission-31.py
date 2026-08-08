class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = 0
        second = 0 # dp[1] = 0 (the cost to reach this step)

        for i in range(2, len(cost) + 1):
            # the cost to reach current step is cost[i - 1] + total cost to reach one step before
            # or cost[i - 2] + total cost to reach two steps before
            third = min(cost[i - 1] + second, cost[i - 2] + first)
            first = second
            second = third
        
        return second
        

        # we want to return dp[len(cost)] at the end (the total cost to reach the end)