class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        stack = []

        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            columnNumber //= 26

            stack.append(chr(offset + ord('A')))
        
        stack.reverse()
        return "".join(stack)