class Solution:
    def decodeString(self, s: str) -> str:
        stringStack = []
        kStack = []

        cur = ""
        k = 0
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stringStack.append(cur)
                kStack.append(k)
                k = 0
                cur = ""
            elif c == "]":
                tmp = cur
                lastString = stringStack.pop()
                lastK = kStack.pop()
                lastString += tmp * lastK
                cur = lastString
            else:
                cur += c
        
        return cur