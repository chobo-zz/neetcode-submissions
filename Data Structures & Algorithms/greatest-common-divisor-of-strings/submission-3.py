class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        def canDivideBoth(length):
            if m % length or n % length:
                return False
            
            factor1 = m // length
            factor2 = n // length

            return str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2

        for i in range(min(m, n), 0, -1):
            if canDivideBoth(i):
                return str1[:i]
        
        return ""