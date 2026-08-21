class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        
        while columnNumber:
            columnNumber -= 1
            digit = columnNumber % 26
            columnNumber //= 26
            char = chr(digit + ord('A'))

            res.append(char)
        
        res.reverse()
        return "".join(res)