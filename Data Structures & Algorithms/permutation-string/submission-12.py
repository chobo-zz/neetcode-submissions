class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Window = [0] * 26
        s2Window = [0] * 26

        for i in range(len(s1)):
            s1Window[ord(s1[i]) - ord('a')] += 1
            s2Window[ord(s2[i]) - ord('a')] += 1
        
        if s1Window == s2Window:
            return True
        
        for i in range(len(s1), len(s2)):
            s2Window[ord(s2[i]) - ord('a')] += 1
            s2Window[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1Window == s2Window:
                return True

        return False