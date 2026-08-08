class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums):
        first = second = 0

        for num in nums:
            third = max(first + num, second)
            first = second
            second = third
        
        return second