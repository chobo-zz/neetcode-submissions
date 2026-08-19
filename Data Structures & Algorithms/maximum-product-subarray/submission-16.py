class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = nums[0]
        curMax = nums[0]
        totalMax = nums[0]

        for num in nums[1:]:
            temp = curMin
            curMin = min(num, num * curMin, num * curMax)
            curMax = max(num, num * temp, num * curMax)
            totalMax = max(totalMax, curMax)
        return totalMax