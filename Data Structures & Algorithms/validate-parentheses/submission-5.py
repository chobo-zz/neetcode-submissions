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
            if c in close_to_open: # if we see close bracket
                if stack and stack[-1] == close_to_open[c]: # if top of stack element is matching, pop it 
                    stack.pop()
                else: # failed to enforce open to close match, return false immediately
                    return False
            else: # if we see open bracket
                stack.append(c)
        return not stack # stack must be empty (no leftover open brackets) to be valid
        
