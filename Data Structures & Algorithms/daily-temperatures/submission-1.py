class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # tuples that store (temp, index)
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # if current temp is greater than top of stack
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((t, i))
        return result