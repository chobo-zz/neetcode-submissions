class Solution:

    def encode(self, strs: List[str]) -> str:
        # use a length + delimiter append approach
        # e.g. input: ["Hello", "World"]
        # e.g. output: "5#Hello5#World"

        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        # read length until we reach delimiter, then iterate length times and store in result list

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res