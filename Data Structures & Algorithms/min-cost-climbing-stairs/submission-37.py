class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = 0
        second = 0

        for i in range(2, len(cost) + 1):
            third = min(cost[i - 1] + second, cost[i - 2] + first)
            first = second
            second = third
        
        return second
