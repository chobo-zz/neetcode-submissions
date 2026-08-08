class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subMax = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += num
            subMax = max(subMax, curSum)
        return subMax