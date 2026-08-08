class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i): # returns LIS starting from position index i
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            memo[i] = res
            return res
        
        LIS = 0
        for i in range(len(nums)):
            LIS = max(LIS, dfs(i))
        return LIS
        