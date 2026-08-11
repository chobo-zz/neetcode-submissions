class Solution:
    def isValid(self, s: str) -> bool:
        cto = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        stack = []

        for c in s:
            if c in cto:
                if not stack or stack[-1] != cto[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
