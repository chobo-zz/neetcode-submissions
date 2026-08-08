class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []

        i, j = 0, 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLen = int(s[i:j])
            j += 1
            i = j + wordLen
            res.append(s[j:i])
        return res