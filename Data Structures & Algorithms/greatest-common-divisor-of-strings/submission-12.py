class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        def canDivide(length):
            if n % length or m % length:
                return False
            
            f1 = n // length
            f2 = m // length

            return str1[:length] * f1 == str1 and str1[:length] * f2 == str2

        for i in range(min(n, m), 0, -1):
            if canDivide(i):
                return str1[:i]
        return ""