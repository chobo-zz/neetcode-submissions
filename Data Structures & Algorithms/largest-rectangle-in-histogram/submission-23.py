class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            startIndex = i

            while stack and stack[-1][1] > h:
                lastIndex, lastHeight = stack.pop()
                startIndex = lastIndex
                maxArea = max(maxArea, (i - lastIndex) * lastHeight)
            
            stack.append((startIndex, h))

        for i, h in stack:
            area = (len(heights) - i) * h
            maxArea = max(maxArea, area)
        
        return maxArea