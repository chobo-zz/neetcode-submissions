class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStart = 0
        resLen = 1
        # odd length
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    resStart = l
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    resStart = l
                l -= 1
                r += 1        
        
        return s[resStart:resStart + resLen]
                
                