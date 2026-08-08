class Solution:
    def decodeString(self, s: str) -> str:
        kStack = []
        cStack = []
        
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                kStack.append(k)
                k = 0

                cStack.append(cur)
                cur = ""

            elif c == "]":
                lastC = cStack.pop()
                lastK = kStack.pop()
                lastC += lastK * cur
                cur = lastC
            else:
                cur += c
        return cur
            
        # a3[c]