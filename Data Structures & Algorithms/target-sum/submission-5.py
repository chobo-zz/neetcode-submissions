class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, remaining):
            if remaining == 0 and i >= len(nums):
                return 1
            
            if i >= len(nums) and remaining != 0:
                return 0
            
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            res = 0
            res += dfs(i + 1, remaining + nums[i])
            res += dfs(i + 1, remaining + nums[i] * -1)

            memo[(i, remaining)] = res
            return res
        
        return dfs(0, target)