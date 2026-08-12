class Solution:
    def decodeString(self, s: str) -> str:
        curStack = []
        kStack = []
        cur = ""
        k = 0

        for c in s:
            if c == "[":
                curStack.append(cur)
                kStack.append(k)
                cur = ""
                k = 0
            elif c == "]":
                lastCur = curStack.pop()
                lastK = kStack.pop()
                lastCur += lastK * cur
                cur = lastCur
            elif c.isdigit():
                k = k * 10 + int(c)
            else:
                cur += c
        
        return cur
        