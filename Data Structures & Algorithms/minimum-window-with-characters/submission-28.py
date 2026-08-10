class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s and t:
            return ""
        
        if not t:
            return ""
        
        if len(t) > len(s):
            return ""
        
        tWindow = Counter(t) # char -> frequency
        sWindow = defaultdict(int) # char -> frequency
        res = []
        resLen = float("inf")
        have = 0
        need = len(tWindow)
        l = 0
        for r in range(len(s)):
            sWindow[s[r]] += 1

            if s[r] in tWindow and sWindow[s[r]] == tWindow[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # try shrinking window from left side
                sWindow[s[l]] -= 1
                if s[l] in tWindow and sWindow[s[l]] < tWindow[s[l]]:
                    have -= 1
                l += 1
        
        if resLen == float("inf"):
            return ""
        
        l, r = res
        return s[l:r + 1]
        




        
