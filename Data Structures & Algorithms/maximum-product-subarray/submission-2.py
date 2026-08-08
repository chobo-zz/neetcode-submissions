class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's algorithm
        # multiplying by negative number might increase total max
        # so keep track of current minimum and current maximum
        # current min/max can also be num itself (start a new subarray) 
        # if multiplying by current min/max hurts new value

        curMin = curMax = nums[0]
        res = nums[0]

        for num in nums[1:]:
            tempCurMax = curMax
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, tempCurMax * num, curMin * num)
            res = max(res, curMax)
        
        return res
