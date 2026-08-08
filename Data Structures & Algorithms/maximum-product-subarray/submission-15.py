class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = curMin = curMax = nums[0]

        for num in nums[1:]:
            tmp = curMin
            curMin = min(num, curMin * num, curMax * num)
            curMax = max(num, tmp * num, curMax * num)
            res = max(res, curMax)

        return res