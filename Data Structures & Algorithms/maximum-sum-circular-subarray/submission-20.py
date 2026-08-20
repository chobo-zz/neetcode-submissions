class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        curMin = nums[0]
        curMax = nums[0]
        total = sum(nums)

        for num in nums[1:]:
            if curMax < 0:
                curMax = 0
            curMax += num
            maxSum = max(maxSum, curMax)

            if curMin > 0:
                curMin = 0
            curMin += num
            minSum = min(minSum, curMin)

        if total == minSum:
            return maxSum
        
        return max(maxSum, total - minSum)