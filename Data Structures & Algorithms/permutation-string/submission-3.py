class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 is bigger than s2, impossible for s2 to contain s1 permutation
        if len(s1) > len(s2): return False

        # initialize hash arrays of character counts
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # add initial counts from s1
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        # if initial counts from both hash arrays are equal, immediately return true
        if s1_counts == s2_counts:
            return True

        # iterate through s2 starting at len(s1) position since we already checked those indices from first for-loop
        # using sliding window, increment and decrement left and right pointer char values
        for i in range(len(s1), len(s2)):
            s2_counts[ord(s2[i]) - ord('a')] += 1
        
            # i - len(s1) means remove the left most char as we slide the window forward
            s2_counts[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_counts == s2_counts:
                return True
        return False
    
        # time: O(s1 + s2) = O(s2)
        # space: O(26 * 2) = O(1)
            
