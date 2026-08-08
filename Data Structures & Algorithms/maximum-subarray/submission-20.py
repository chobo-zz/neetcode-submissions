class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 0
        
        for num in nums:
            if curMax < 0:
                curMax = 0
            
            curMax += num
            res = max(res, curMax)
        
        return res