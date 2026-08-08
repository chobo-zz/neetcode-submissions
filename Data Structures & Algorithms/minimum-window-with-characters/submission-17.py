class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t or not s:
            return ""

        countT = Counter(t)
        have = 0
        need = len(countT)
        res = ""
        minLen = float("inf")
        l = 0
        window = defaultdict(int)

        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    res = s[l:r + 1]
                    minLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return res
