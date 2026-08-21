class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            if c == ")":
                leftMin -= 1
                leftMax -= 1
            if c == "*":
                leftMin -= 1
                leftMax += 1
            
            if leftMin < 0:
                leftMin = 0

            if leftMax < 0:
                return False
            
        
        return leftMin == 0