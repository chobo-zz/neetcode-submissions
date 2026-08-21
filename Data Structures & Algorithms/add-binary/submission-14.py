class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        res = []

        i, j, carry = 0, 0, 0

        while i < len(a) or j < len(b):
            first = int(a[i]) if i < len(a) else 0
            second = int(b[j]) if j < len(b) else 0
            total = first + second + carry
            digit = total % 2
            carry = total // 2

            i += 1
            j += 1
            res.append(digit)

        if carry:
            res.append(carry)

        res = res[::-1]
        res = map(str, res)
        return "".join(res)
