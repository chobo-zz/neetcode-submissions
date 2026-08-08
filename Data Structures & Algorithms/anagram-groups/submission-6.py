class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = collections.defaultdict(list)

        for word in strs:
            bucket = [0] * 26
            for char in word:
                unicode = ord(char) - ord('a')
                bucket[unicode] += 1
            key = tuple(bucket)
            mp[key].append(word)
        
        return list(mp.values())