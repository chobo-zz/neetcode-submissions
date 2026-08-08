class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        downOne = 0
        downTwo = 0

        for i in range(2, len(cost) + 1):
            temp = downOne
            downOne = min(downOne + cost[i - 1], downTwo + cost[i - 2])
            downTwo = temp
        return downOne