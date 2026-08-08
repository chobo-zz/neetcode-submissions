class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                lastIndex = stack.pop()[0]
                res[lastIndex] = index - lastIndex
            stack.append((index, temp))

        return res