class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        
        columnNumber -= 1 # handle off by one index issue when we convert to unicode character
    
        return self.convertToTitle(columnNumber // 26) + chr((columnNumber % 26) + ord('A'))