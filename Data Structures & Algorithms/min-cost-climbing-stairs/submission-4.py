class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = second = 0

        for i in range(2, len(cost) + 1):
            third = min(cost[i - 2] + first, cost[i - 1] + second)
            first = second
            second = third
            
        return second