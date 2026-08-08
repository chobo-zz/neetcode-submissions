class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, runningSum):
            if i >= len(nums) and runningSum == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            if (i, runningSum) in memo:
                return memo[(i, runningSum)]

            res = 0
            res += dfs(i + 1, runningSum - nums[i])
            res += dfs(i + 1, runningSum + nums[i])
            memo[(i, runningSum)] = res
            return res
        
        return dfs(0, 0)