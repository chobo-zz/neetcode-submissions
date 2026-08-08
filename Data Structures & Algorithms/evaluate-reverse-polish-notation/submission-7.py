class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) - int(a))
            elif c == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(int(b) / int(a)))
            else:
                stack.append(int(c))
        
        return stack.pop()