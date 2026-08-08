class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # initialize left and right pointers to index 0
        # check if char at right pointer exists in set (duplicate)
        # if so, then we must nudge left pointer by one, remove char at left pointer from set
        # if not, then we keep nudging right pointer by one, adding new char to set
        # during this, we must keep calculating max substring with formula: r - l + 1 (plus one because zero indexed)
        # return max result

        char_set = set()
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res
                
            

            
