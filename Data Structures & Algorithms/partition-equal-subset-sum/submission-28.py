class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False # odd sum length, cant partition into halves
        
        half = total // 2

        memo = {}

        def dfs(i, runningSum): # returns whether runningSum == half starting at this index
            if runningSum == half:
                return True
            
            if i >= len(nums) or runningSum > half:
                return False
            
            if (i, runningSum) in memo:
                return memo[(i, runningSum)]
            
            memo[(i, runningSum)] = dfs(i + 1, runningSum + nums[i]) or dfs(i + 1, runningSum)
            return memo[(i, runningSum)]
        
        return dfs(0, 0)
