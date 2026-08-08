class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cto = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in cto:
                if stack and stack[-1] == cto[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack