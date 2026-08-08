class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            wordLen = len(word)
            res += str(wordLen) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLen = int(s[i:j])
            i = j + 1
            word = s[i:i + wordLen]
            res.append(word)
            i = i + wordLen
        return res
        


