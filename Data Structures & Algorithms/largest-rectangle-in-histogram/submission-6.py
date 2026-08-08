class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = heights[0]
        stack = [] # index, height

        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append((start, v))
        
        while stack:
            index, height = stack.pop()
            res = max(res, height * (len(heights) - index))
        
        return res
