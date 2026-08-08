class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        r = 0

        while r < len(nums) - 1:
            farthest = r

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # if we couldn't expand past current r, we're stuck
            if farthest == r:
                return False

            l = r + 1
            r = farthest
        
        return True