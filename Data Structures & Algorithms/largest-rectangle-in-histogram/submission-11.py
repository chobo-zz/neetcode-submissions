class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # holds (index, height) of each bar
        maxArea = 0

        for index, height in enumerate(heights):
            start = index

            while stack and stack[-1][1] > height:
                prevIndex, prevHeight = stack.pop()
                maxArea = max(maxArea, prevHeight * (index - prevIndex))
                start = prevIndex
            stack.append((start, height))
            
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        
        return maxArea