class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goalpost = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goalpost:
                goalpost = i
        
        return goalpost == 0