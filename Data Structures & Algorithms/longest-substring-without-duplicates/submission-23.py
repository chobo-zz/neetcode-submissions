class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        cur = 0

        if not s:
            return 0
        
        l = r = 0


        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                cur -= 1
            seen.add(s[r])
            cur += 1
            res = max(res, cur)
            r += 1
        return res