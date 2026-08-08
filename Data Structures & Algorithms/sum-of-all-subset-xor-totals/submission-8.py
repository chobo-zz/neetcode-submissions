class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total = total | num
        
        return total * 2 ** (len(nums) - 1)