class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        gasLeft = 0
        res = 0
        for i in range(len(gas)):
            gasLeft += gas[i] - cost[i]

            if gasLeft < 0:
                gasLeft = 0
                res = i + 1
        
        return res