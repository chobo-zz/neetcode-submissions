class Solution:
    def isValid(self, s: str) -> bool:
        # leverage stack to ensure bracket-type matching
        # leverage dict as a "key" or "legend" to map each close bracket to its appropriate open bracket
        # we push all open-type brackets to the stack
        # when we encounter a close bracket, we pop from the stack and ensure its matching according to dict
        # at the end, stack should be empty. if not, return false

        stack = []
        close_to_open = { 
            ')': '(', 
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        
