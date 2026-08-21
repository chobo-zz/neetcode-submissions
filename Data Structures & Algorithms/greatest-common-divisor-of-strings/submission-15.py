class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        def canDivide(length):
            if n % length or m % length: # 2
                return False
            
            factor1 = n // length # 3
            factor2 = m // length # 2

            return str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2
            

        for length in range(min(n, m), 0, -1):
            if canDivide(length):
                return str1[:length]
        
        return ""

        # ABABAB 
        # AB