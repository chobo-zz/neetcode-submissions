class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        memo = {}

        def dfs(i, m): # returns minimized largest sum split from nums[i:] with m remaining groups
            if i == len(nums):
                return 0 if m == 0 else float("inf")
            
            if m == 0:
                return float("inf")
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            curSum = 0
            res = float("inf")
            for j in range(i, len(nums) - m + 1):
                curSum += nums[j]
                largest = max(curSum, dfs(j + 1, m - 1))
                res = min(res, largest)
            
            memo[(i, m)] = res
            return res
        
        return dfs(0, k)