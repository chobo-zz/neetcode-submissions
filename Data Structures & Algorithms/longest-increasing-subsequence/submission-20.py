class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # (i -> LIS)

        def dfs(i): # returns LIS from starting index i
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            res = 1
            for j in range(i + 1, len(nums)): # choose or skip j'th element: [1, 100, 2,3,4,5] <- skipping j = 1 gives LIS
                if nums[i] < nums[j]:
                    res = max(res, 1 + dfs(j)) # comparison to see whether taking j'th element derives LIS
            memo[i] = res
            return res

        LIS = 1
        for i in range(len(nums)):
            LIS = max(LIS, dfs(i))
        
        return LIS