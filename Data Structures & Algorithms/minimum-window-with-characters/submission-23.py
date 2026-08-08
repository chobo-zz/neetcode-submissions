class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t or not s:
            return ""

        have = 0
        count = Counter(t)
        need = len(count)
        window = defaultdict(int)
        minLen = float("inf")
        l = 0
        res = ""

        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == count[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    res = s[l: r + 1]
                
                window[s[l]] -= 1
                if window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        
        return res