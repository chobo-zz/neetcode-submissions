class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        
        columnNumber -= 1
        digit = columnNumber % 26 # 31 -> 5 -> F character
        nextColumnNumber = columnNumber // 26 # 31 -> 1 -> A character
        # input of num 32 to return AF

        return self.convertToTitle(nextColumnNumber) + chr(digit + ord('A'))
