class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        half = total // 2
        memo = {}

        def dfs(i, curSum):
            if i == len(nums):
                return curSum == half
            
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            memo[(i, curSum)] = False
            if dfs(i + 1, curSum + nums[i]):
                memo[(i, curSum)] = True
                return True
            return dfs(i + 1, curSum)
            
        return dfs(0, 0)
