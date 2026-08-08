class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        res = 1

        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            LIS = 1

            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return LIS
        
        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res
                
            