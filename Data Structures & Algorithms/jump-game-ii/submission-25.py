class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        l, r = 0, 0
        level = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            level += 1
        
        return level

            