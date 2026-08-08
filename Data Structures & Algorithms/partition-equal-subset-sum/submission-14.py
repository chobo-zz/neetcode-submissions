class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2:
            return False
        
        target = totalSum // 2

        memo = {} # (i, runningSum) -> can reach target

        def dfs(i, runningSum): # return whether we can reach target sum from index i
            if runningSum == target:
                return True
            
            if runningSum > target or i >= len(nums):
                return False
            
            if (i, runningSum) in memo:
                return memo[(i, runningSum)]
            
            memo[(i, runningSum)] = (
                dfs(i + 1, runningSum + nums[i]) or
                dfs(i + 1, runningSum)
            )
            return memo[(i, runningSum)]

        return dfs(0, 0)