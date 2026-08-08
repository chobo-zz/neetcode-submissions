class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            return 0
        
        res = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            bottleneck = min(heights[l], heights[r])
            area = bottleneck * (r - l)
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
