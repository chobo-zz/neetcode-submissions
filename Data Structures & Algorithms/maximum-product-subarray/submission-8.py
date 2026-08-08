class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's algorithm (left -> right, make a choice each step: 
        # start new max by choosing current number or continue multiplying to max)

        # multiplying two negatives can produce the positive max
        # so we should keep track of two vars: curMax, curMin
        res = curMax = curMin = nums[0]
        for num in nums[1:]:
            temp = curMin
            curMin = min(num, num * curMin, num * curMax)
            curMax = max(num, num * temp, num * curMax)
            res = max(res, curMax)

        return res