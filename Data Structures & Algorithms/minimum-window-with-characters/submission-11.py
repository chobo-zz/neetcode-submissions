class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        count = Counter(t)
        window = defaultdict(int)
        l = 0
        have = 0
        need = len(count)
        res = [0, 0]
        resLen = float("infinity")

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

