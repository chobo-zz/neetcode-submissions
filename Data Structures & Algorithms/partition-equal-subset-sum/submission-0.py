class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2:
            return False

        memo = {} # (index, current running sum): True/False
        
        def dfs(i, currSum):
            if currSum * 2 == totalSum:
                return True
            
            if currSum > totalSum // 2 or i >= len(nums):
                return False

            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            res = dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum)

            memo[(i, currSum)] = res
            return res
        
        return dfs(0, 0)
