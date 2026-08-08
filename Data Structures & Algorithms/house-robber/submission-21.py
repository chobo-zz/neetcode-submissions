class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        first = nums[0] # dp[0] = house at index 0 (only option)
        second = max(nums[0], nums[1]) # dp[1] = max of house at index 0 or index 1
        # dp is storing what is the max possible robbed up to index i

        for i in range(2, len(nums)):
            third = max(first + nums[i], second)
            first = second
            second = third
        
        return second