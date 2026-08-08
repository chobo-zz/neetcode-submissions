class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bucket = [0] * 26

        for c in s:
            unicode = ord(c) - ord('a')
            bucket[unicode] += 1
        
        for c in t:
            unicode = ord(c) - ord('a')
            bucket[unicode] -= 1
        
        for count in bucket:
            if count:
                return False
        
        return True
