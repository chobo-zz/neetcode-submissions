class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0

        curSum = 0
        minLen = len(nums) + 1
        while r < len(nums):
            curSum += nums[r]
            

            while curSum >= target:
                minLen = min(minLen, r - l + 1)
                curSum -= nums[l]
                l += 1
            r += 1
        return 0 if minLen == len(nums) + 1 else minLen

