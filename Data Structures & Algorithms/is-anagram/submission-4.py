class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = [0] * 26

        for i in range(len(s)):
            seen[ord(t[i]) - ord('a')] += 1
            seen[ord(s[i]) - ord('a')] -= 1
        
        for count in seen:
            if count != 0:
                return False
        
        return True
