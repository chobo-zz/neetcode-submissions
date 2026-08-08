class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = heights[0]
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                res = max(res, area)
                start = index
            stack.append((start, h))
        
        while stack:
            i, h = stack.pop()
            res = max(res, h * (len(heights) - i))
        
        return res