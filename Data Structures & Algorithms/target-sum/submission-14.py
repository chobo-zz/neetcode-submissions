class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, curSum):
            if i == len(nums):
                return curSum == target
            
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            
            add = dfs(i + 1, curSum + nums[i])
            subtract = dfs(i + 1, curSum - nums[i])

            memo[(i, curSum)] = add + subtract
            return memo[(i, curSum)]

        return dfs(0, 0)