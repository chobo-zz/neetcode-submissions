class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0

        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(s)):
            if (i + 1) < len(s) and mapping[s[i + 1]] > mapping[s[i]]:
                res -= mapping[s[i]]
            else:
                res += mapping[s[i]]
        
        return res
            