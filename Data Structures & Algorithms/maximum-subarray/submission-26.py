class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curSum = nums[0]

        for num in nums[1:]:
            if curSum < 0:
                curSum = 0
            curSum += num
            res = max(res, curSum)
        
        return res