class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        i, j, carry = len(a) - 1, len(b) - 1, 0

        while i >= 0 or j >= 0:
            firstNum = int(a[i]) if i >= 0 else 0
            secondNum = int(b[j]) if j >= 0 else 0
            curSum = firstNum + secondNum + carry
            digit = curSum % 2
            carry = curSum // 2
            res.append(digit)

            i -= 1
            j -= 1
        
        if carry:
            res.append(carry)
        
        res = res[::-1]
        res = map(str, res)
        return "".join(res)