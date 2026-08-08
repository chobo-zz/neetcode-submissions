class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax = leftMin = 0

        for c in s:
            if c == "(":
                leftMax += 1
                leftMin += 1
            if c == ")":
                leftMax -= 1
                leftMin -= 1
            if c == "*":
                leftMax += 1
                leftMin -= 1
            
            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False
        return leftMin == 0