class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        
        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            third = max(first + nums[i], second)
            first = second
            second = third
        
        return second