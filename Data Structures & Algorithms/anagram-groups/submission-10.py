class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list) # bucket count tuple -> list of strings
        for str in strs:
            bucket = [0] * 26

            for c in str:
                bucket[ord(c) - ord('a')] += 1
            seen[tuple(bucket)].append(str)
        
        return list(seen.values())
            