class Solution:
    def rob(self, nums: List[int]) -> int:
        first = second = 0

        for num in nums:
            third = max(first + num, second)
            first = second
            second = third
        
        return max(first, second)
