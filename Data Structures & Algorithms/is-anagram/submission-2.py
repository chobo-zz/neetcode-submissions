class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
        for i in range(len(t)):
            counts[t[i]] = counts.get(t[i], 0) - 1
        
        return all(v == 0 for v in counts.values())