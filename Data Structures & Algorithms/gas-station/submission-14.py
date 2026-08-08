class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        startingIndex = 0
        curGas = 0
        for i in range(len(gas) - 1):
            curGas += gas[i] - cost[i]
            if curGas < 0:
                curGas = 0
                startingIndex = i + 1
        
        return startingIndex