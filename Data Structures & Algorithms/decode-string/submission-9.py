class Solution:
    def decodeString(self, s: str) -> str:
        idx = 0
        def helper():
            nonlocal idx
            cur = ""
            k = 0

            while idx < len(s):
                c = s[idx]
                if c == "[":
                    idx += 1
                    subresult = k * helper()
                    k = 0
                    cur += subresult
                elif c == "]":
                    return cur
                elif c.isdigit():
                    k = k * 10 + int(c)
                else: # character case
                    cur += c
                idx += 1
            return cur
        
        return helper()


        