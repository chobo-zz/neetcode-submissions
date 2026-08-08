class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordBucket = defaultdict(list) # tuple of char bucket -> list of words

        for word in strs:
            charBucket = [0] * 26

            for c in word:
                charBucket[ord(c) - ord('a')] += 1
            wordBucket[tuple(charBucket)].append(word)
        
        return list(wordBucket.values())