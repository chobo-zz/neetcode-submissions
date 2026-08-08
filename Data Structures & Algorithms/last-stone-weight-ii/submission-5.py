class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        memo = {}

        def dfs(i, curSum): # returns min sum difference between curSum and otherSum pile
            if i == len(stones):
                otherSum = totalSum - curSum
                return abs(curSum - otherSum)
            
            if (i, curSum) in memo:
                return memo[(i, curSum)]
                
            take = dfs(i + 1, curSum + stones[i])
            skip = dfs(i + 1, curSum)

            minSumDiff = min(take, skip)
            memo[(i, curSum)] = minSumDiff

            return minSumDiff
        
        return dfs(0, 0)
        