class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        
        columnNumber -= 1
        offset = columnNumber % 26
        columnNumber //= 26

        return self.convertToTitle(columnNumber) + chr(offset + ord('A'))