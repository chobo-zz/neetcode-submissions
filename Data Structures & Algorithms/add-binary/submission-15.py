class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j, carry = len(a) - 1, len(b) - 1, 0

        while i >= 0 or j >= 0:
            first = int(a[i]) if i >= 0 else 0
            second = int(b[j]) if j >= 0 else 0

            total = first + second + carry
            digit = total % 2
            carry = total // 2
            res.append(digit)

            i -= 1
            j -= 1
        
        if carry:
            res.append(carry)
        
        res = res[::-1]
        res = map(str, res)
        return "".join(res)