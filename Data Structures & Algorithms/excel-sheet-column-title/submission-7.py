class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            digit = columnNumber % 26
            columnNumber //= 26
            res.append(chr(digit + ord('A')))

        res.reverse()
        return "".join(res)