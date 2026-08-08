class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subMax = nums[0]
        curMax = 0

        for num in nums:
            if curMax < 0:
                curMax = 0
            curMax += num
            subMax = max(subMax, curMax)
        
        return subMax