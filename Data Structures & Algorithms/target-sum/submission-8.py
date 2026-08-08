class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (i, remaining) -> num ways to reach target

        def dfs(i, remaining):
            if remaining == 0 and i >= len(nums):
                return 1

            if i >= len(nums) and remaining != 0:
                return 0
            
            memo[(i, remaining)] = dfs(i + 1, remaining - nums[i]) + dfs(i + 1, remaining + nums[i])

            return memo[(i, remaining)]

        return dfs(0, target)
        