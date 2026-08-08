class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, remaining): # returns num ways to sum to remaining starting from index i
            if i >= len(nums) and remaining == 0:
                return 1
            
            if i >= len(nums):
                return 0
            
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            memo[(i, remaining)] = dfs(i + 1, remaining - nums[i]) + dfs(i + 1, remaining + nums[i])
            return memo[(i, remaining)]
        
        return dfs(0, target)