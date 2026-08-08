class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = defaultdict(int)
        res = 0

        while r < len(s):
            counts[s[r]] += 1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res