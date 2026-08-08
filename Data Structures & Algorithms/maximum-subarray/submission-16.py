class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            curMax = max(nums[i], nums[i] + curMax)

            if curMax > res:
                res = curMax
        
        return res