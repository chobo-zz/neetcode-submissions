class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        ans = 0
        curGas = 0
        for i in range(len(gas)):
            curGas += gas[i] - cost[i]
            if curGas < 0:
                ans = i + 1
                curGas = 0
        return ans