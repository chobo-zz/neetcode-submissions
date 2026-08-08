class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        LIS = 1

        def dfs(i): # function returns what is max LIS at given index
            if memo[i] != -1:
                return memo[i]
            
            res = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            memo[i] = res
            return res
        
        for i in range(len(nums)):
            LIS = max(LIS, dfs(i))

        return LIS