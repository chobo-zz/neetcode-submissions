class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            digit = columnNumber % 26
            res.append(chr(digit + ord('A')))
            columnNumber //= 26
        
        return "".join(res[::-1])
