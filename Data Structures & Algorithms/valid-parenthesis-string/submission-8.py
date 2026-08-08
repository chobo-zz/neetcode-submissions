class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax, leftMin = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            
            if leftMin < 0:
                leftMin = 0

            if leftMax < 0:
                return False
        
        return leftMin == 0