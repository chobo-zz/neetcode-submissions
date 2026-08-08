class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""

        columnNumber -= 1

        return self.convertToTitle(columnNumber // 26) + chr((columnNumber % 26) + ord('A'))