class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = [] # (index, height)
        maxArea = 0

        for idx, hei in enumerate(heights):
            start = idx

            while stack and stack[-1][1] > hei:
                lastIdx, lastHei = stack.pop()
                area = (idx - lastIdx) * lastHei
                maxArea = max(area, maxArea)
                start = lastIdx
            stack.append((start, hei))
        
        for idx, hei in stack:
            maxArea = max(maxArea, (hei * (len(heights) - idx)))
        
        return maxArea