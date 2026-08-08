class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0

        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            curArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(curArea, maxArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea