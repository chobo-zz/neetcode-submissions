class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        columnNumber -= 1

        remainder = columnNumber % 26
        char = chr(ord('A') + remainder)
        columnNumber //= 26

        res = self.convertToTitle(columnNumber) + char 
        return res

