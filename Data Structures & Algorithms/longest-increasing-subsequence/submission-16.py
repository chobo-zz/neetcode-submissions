class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # (i -> LIS starting from that index)
        LIS = 1
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, 1 + dfs(j))
            memo[i] = res
            return res

        for i in range(len(nums)):
            LIS = max(LIS, dfs(i))
        
        return LIS