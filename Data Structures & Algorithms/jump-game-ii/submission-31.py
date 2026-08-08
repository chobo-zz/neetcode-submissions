class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l, r = 0, 0
        farthest = 0
        jumps = 0
        while r < len(nums) - 1:
            
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            
            l = r + 1
            r = farthest
            jumps += 1
        
        return jumps