class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1


        while i >= 0 or j >= 0:
            aDigit = int(a[i]) if i >= 0 else 0
            bDigit = int(b[j]) if j >= 0 else 0

            sumDigit = (aDigit + bDigit + carry)
            newDigit = sumDigit % 2
            carry = sumDigit // 2
            res.append(newDigit)

            i -= 1
            j -= 1
        
        if carry:
            res.append(carry)
        
        res.reverse()
        return "".join(map(str, res))

