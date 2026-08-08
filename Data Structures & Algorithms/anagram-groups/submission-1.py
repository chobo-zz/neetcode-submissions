class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hash map which stores char counts -> list of words
        # hash map key is a 26-length "list" (tuple) that stores character counts
        # hash map value is a list containing the original word

        # set up a hash map containing default keys
        # iterate through strs
        # create a temporary "key" list of 26-length
        # iterate through each str character
        # increment char count by 1 in our temp key list if seen
        # convert the "key" list into a tuple and map the original string to that tuple
        # finally, convert the map values into a list and return

        my_map = defaultdict(list)

        for word in strs:
            counts = [0] * 26

            for char in word:
                counts[ord(char) - ord('a')] += 1
            key_tuple = tuple(counts)
            my_map[key_tuple].append(word)
        
        return list(my_map.values())