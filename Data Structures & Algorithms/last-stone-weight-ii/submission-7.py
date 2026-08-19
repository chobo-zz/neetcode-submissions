class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        total = sum(stones)

        def dfs(i, curSum):
            if i == len(stones):
                otherSum = total - curSum
                return abs(curSum - otherSum)
            
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            
            take = dfs(i + 1, curSum + stones[i])
            skip = dfs(i + 1, curSum)
            minDiff = min(take, skip)

            memo[(i, curSum)] = minDiff
            return minDiff
        
        return dfs(0, 0)