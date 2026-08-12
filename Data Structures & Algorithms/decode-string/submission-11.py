class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def helper():
            nonlocal i
            cur = ""
            k = 0

            while i < len(s):
                c = s[i]

                if c == "[":
                    i += 1
                    cur += k * helper()
                    k = 0
                elif c == "]":
                    return cur
                elif c.isdigit():
                    k = k * 10 + int(c)
                else:
                    cur += c
                
                i += 1
            
            return cur
        
        return helper()