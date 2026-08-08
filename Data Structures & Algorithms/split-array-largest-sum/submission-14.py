class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        memo = {}
        n = len(nums)

        def dfs(i, k): # returns minimized largest sum for nums[i:] and k left groups to form
            if i == n and k == 0:
                return 0
            
            if k == 0:
                return float("inf")
            
            if (i, k) in memo:
                return memo[(i, k)]
            
            curSum = 0
            res = float("inf")
            for j in range(i, n - k + 1):
                curSum += nums[j]
                largest = max(curSum, dfs(j + 1, k - 1))
                res = min(res, largest)
            memo[(i, k)] = res
            return res
        
        return dfs(0, k)
        