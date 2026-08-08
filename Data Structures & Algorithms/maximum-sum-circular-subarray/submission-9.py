class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMin = nums[0]
        curMax = nums[0]
        totalMax = nums[0]
        totalMin = nums[0]
        totalSum = nums[0]
        
        for num in nums[1:]:
            # kadane's for max
            if curMax < 0:
                curMax = 0
            curMax += num
            totalMax = max(totalMax, curMax)

            # kadane's for min
            if curMin > 0:
                curMin = 0
            curMin += num
            totalMin = min(totalMin, curMin)

            totalSum += num
        
        if totalSum == totalMin:
            return totalMax
        
        return max(totalMax, totalSum - totalMin)