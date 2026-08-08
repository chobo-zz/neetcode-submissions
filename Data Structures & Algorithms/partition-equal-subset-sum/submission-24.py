class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        memo = {}
        
        def dfs(i, runningSum): # returns whether we can sum up to half starting at index i
            if runningSum == half:
                return True
            
            if i >= len(nums) or runningSum > half:
                return False
            
            if (i, runningSum) in memo:
                return memo[(i, runningSum)]
            
            memo[(i, runningSum)] = dfs(i + 1, runningSum + nums[i]) or dfs(i + 1, runningSum)

            return memo[(i, runningSum)]
        
        return dfs(0, 0)


