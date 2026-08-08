class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        set1 = [0] * 26
        set2 = [0] * 26

        for i in range(len(s1)):
            set1[ord(s1[i]) - ord('a')] += 1
            set2[ord(s2[i]) - ord('a')] += 1
        
        if set1 == set2:
            return True
        
        for i in range(len(s1), len(s2)):
            set2[ord(s2[i]) - ord('a')] += 1
            set2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if set1 == set2:
                return True
        return False
        