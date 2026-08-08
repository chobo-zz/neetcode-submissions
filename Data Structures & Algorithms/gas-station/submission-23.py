class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)
        if totalGas < totalCost:
            return -1
        
        res = 0
        curGas = 0
        for i in range(len(gas)):
            curGas += gas[i] - cost[i]
            if curGas < 0:
                res = i + 1
                curGas = 0
        
        return res