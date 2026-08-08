class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hash map which stores char counts -> list of words
        # hash map key is a 26-length list that stores character counts 
        # (e.g. index 4 corresponds to letter 'd', and the value is a number denoting how many times it was seen)
        # hash map value is a list containing the original word

        # set up a hash map containing default keys
        # iterate through strs
        # create a temporary "key" list of 26-length
        # iterate through each str character
        # increment char count by 1 in our temp key list if seen
        # convert the "key" list into a tuple and map the original string to that tuple
        # finally, convert the map values into a list and return

        mp = collections.defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for char in word:
                uni = ord(char) - ord('a')
                counts[uni] += 1
            key = tuple(counts)
            mp[key].append(word)
        return list(mp.values())
