class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        cur = 0

        if not s:
            return 0
        
        l = 0


        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r])
            length = r - l + 1
            res = max(res, length)
        return res