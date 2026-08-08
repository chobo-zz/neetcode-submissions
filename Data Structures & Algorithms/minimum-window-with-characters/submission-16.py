class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t or not s:
            return ""
        
        countT = Counter(t)
        have = 0
        need = len(countT)
        window = defaultdict(int)
        l = 0
        maxLen = float("infinity")
        res = ""
        
        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < maxLen:
                    maxLen = r - l + 1
                    res = s[l:r + 1]
                
                window[s[l]] -= 1
                
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return res


                
