class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curSum = nums[0]

        for i in range(1, len(nums)):
            if curSum < 0:
                curSum = 0
            
            curSum += nums[i]
            res = max(res, curSum)
        
        return res