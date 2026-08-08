class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2:
            return False

        target = totalSum // 2
        
        memo = {} # (index i, runningSum) -> equal to target

        def dfs(i, runningSum):
            if runningSum == target:
                return True
            
            if i >= len(nums):
                return False
            
            if (i, runningSum) in memo:
                return memo[(i, runningSum)]
            
            memo[(i, runningSum)] = dfs(i + 1, runningSum) or dfs(i + 1, nums[i] + runningSum)
            return memo[(i, runningSum)]
        

        return dfs(0, 0)