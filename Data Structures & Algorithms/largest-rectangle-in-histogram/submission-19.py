class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = []
        res = 0
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][0] > height:
                prevHeight, prevStart = stack.pop()
                res = max(res, ((index - prevStart) * prevHeight))
                start = prevStart

            stack.append((height, start))
        
        for height, index in stack:
            res = max(res, (height * (len(heights) - index)))
        return res
            