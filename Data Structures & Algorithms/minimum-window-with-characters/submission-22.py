class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t or not s:
            return ""

        count = Counter(t)
        have = 0
        need = len(count)
        window = defaultdict(int)
        minLen = float("inf")
        l, r = 0, 0
        res = ""

        while r < len(s):
            window[s[r]] += 1

            if window[s[r]] == count[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r + 1]
                
                window[s[l]] -= 1
                if window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        
            r += 1
        
        return res
            