class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = curMin = curMax = nums[0]

        for num in nums[1:]:
            temp = curMin
            curMin = min(num, curMin * num, curMax * num)
            curMax = max(num, curMax * num, temp * num)
            res = max(res, curMax)
        return res