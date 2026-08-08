class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's algorithm (left -> right, make a choice each step: 
        # start new max or continue adding to max)

        # multiplying two negatives can produce positive max
        # so we should keep track of curMax, curMin
        res = nums[0]
        curMin = 1
        curMax = 1
        for num in nums:
            temp = curMin
            curMin = min(num, num * curMin, num * curMax)
            curMax = max(num, num * temp, num * curMax)
            res = max(res, curMax)

        return res