class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 1
        resInd = 0
        for i in range(len(s)):
            # check odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resInd = l
                l -= 1
                r += 1
            
            # check even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resInd = l
                l -= 1
                r += 1
        
        return s[resInd:resInd + resLen]
