class Solution:
    def canJump(self, nums: List[int]) -> bool:
        earliest = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= earliest:
                earliest = i
            
        return True if earliest == 0 else False
                
