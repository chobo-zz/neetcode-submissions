class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucketToWords = defaultdict(list) # char count bucket tuple -> list of words

        for word in strs:
            bucket = [0] * 26
            for c in word:
                bucket[ord(c) - ord('a')] += 1
            bucketToWords[tuple(bucket)].append(word)
        
        return list(bucketToWords.values())